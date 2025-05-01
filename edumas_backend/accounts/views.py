from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from drf_spectacular.utils import extend_schema
from .models import UserProfile, CustomUser
from .serializers import (
    UserProfileSerializer, 
    CustomUserSerializer,
    UserRegistrationSerializer,
    LoginSerializer
)
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import EmailVerificationToken, CustomUser
from django.utils import timezone
import uuid


class UserRegistrationView(APIView):
    """
    Register a new user with profile in a single request
    """
    permission_classes = [permissions.AllowAny]
    
    @extend_schema(
        summary="Register a new user with profile",
        request=UserRegistrationSerializer,
        responses={201: UserProfileSerializer},
    )
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            profile = serializer.save()
            return Response(
                UserProfileSerializer(profile).data, 
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    """
    Authenticate a user and return JWT tokens
    """
    permission_classes = [permissions.AllowAny]
    
    @extend_schema(
        summary="Login and get JWT tokens",
        request=LoginSerializer,
        responses={
            200: {
                "type": "object", 
                "properties": {
                    "refresh": {"type": "string"},
                    "access": {"type": "string"},
                    "user": {"type": "object"}
                }
            },
            401: {"description": "Invalid credentials or email not verified"},
            400: {"description": "Invalid request"}
        },
    )
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            
            # Authenticate user
            user = authenticate(request, username=email, password=password)
            
            if user:
                # Check if email is verified
                if not user.email_verified:
                    return Response(
                        {"error": "Please verify your email before logging in."},
                        status=status.HTTP_401_UNAUTHORIZED
                    )
                
                # Generate JWT tokens
                refresh = RefreshToken.for_user(user)
                
                # Get user profile data
                try:
                    profile = user.profile
                    user_type = profile.user_type
                    name = f"{profile.first_name} {profile.last_name}"
                except:
                    user_type = None
                    name = None
                
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'user': {
                        'id': user.id,
                        'email': user.email,
                        'user_type': user_type,
                        'name': name,
                        'email_verified': user.email_verified
                    }
                })
            else:
                return Response(
                    {"error": "Invalid credentials"}, 
                    status=status.HTTP_401_UNAUTHORIZED
                )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    """
    Blacklist the refresh token to logout
    """
    permission_classes = [permissions.IsAuthenticated]
    
    @extend_schema(
        summary="Logout by blacklisting the refresh token",
        request={
            "type": "object",
            "properties": {
                "refresh": {"type": "string"}
            },
            "required": ["refresh"]
        },
        responses={205: None},
    )
    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)



class CustomAuthToken(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'user_type': user.user_type
        })    

class VerifyEmailView(APIView):
    """
    Verify a user's email address using a verification token
    """
    permission_classes = [permissions.AllowAny]
    
    @extend_schema(
        summary="Verify user email address",
        parameters=[
            {
                'name': 'token',
                'in': 'path',
                'description': 'Email verification token',
                'required': True,
                'type': 'string',
                'format': 'uuid'
            }
        ],
        responses={
            200: {"description": "Email verified successfully"},
            400: {"description": "Invalid token or token expired"},
            404: {"description": "Token not found"}
        },
    )
    def get(self, request, token):
        try:
            # Validate UUID format
            token_uuid = uuid.UUID(token)
            
            # Find the token
            verification_token = EmailVerificationToken.objects.select_related('user').get(token=token_uuid)
            
            # Check if token is expired
            if not verification_token.is_valid():
                return Response(
                    {"error": "Verification token has expired. Please request a new one."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Mark user as verified and active
            user = verification_token.user
            user.email_verified = True
            user.is_active = True
            user.save()
            
            # Delete the token as it's been used
            verification_token.delete()
            
            return Response(
                {"message": "Email verified successfully. You can now log in."},
                status=status.HTTP_200_OK
            )
            
        except (ValueError, uuid.BadUUIDError):
            return Response(
                {"error": "Invalid verification token format."},
                status=status.HTTP_400_BAD_REQUEST
            )
        except EmailVerificationToken.DoesNotExist:
            return Response(
                {"error": "Verification token not found."},
                status=status.HTTP_404_NOT_FOUND
            )

class ResendVerificationEmailView(APIView):
    """
    Resend verification email to the user
    """
    permission_classes = [permissions.AllowAny]
    
    @extend_schema(
        summary="Resend verification email",
        request={
            "type": "object",
            "properties": {
                "email": {"type": "string", "format": "email"}
            },
            "required": ["email"]
        },
        responses={
            200: {"description": "Verification email sent"},
            400: {"description": "Invalid email or account already verified"},
            404: {"description": "User not found"}
        },
    )
    def post(self, request):
        email = request.data.get('email')
        
        if not email:
            return Response(
                {"error": "Email is required."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            user = CustomUser.objects.get(email=email)
            
            # Check if user is already verified
            if user.email_verified:
                return Response(
                    {"error": "Email is already verified."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Delete any existing tokens
            EmailVerificationToken.objects.filter(user=user).delete()
            
            # Create new token
            token = EmailVerificationToken.objects.create(user=user)
            
            # Send verification email
            from .utils import send_verification_email
            send_verification_email(user, token)
            
            return Response(
                {"message": "Verification email sent."},
                status=status.HTTP_200_OK
            )
            
        except CustomUser.DoesNotExist:
            return Response(
                {"error": "User with this email does not exist."},
                status=status.HTTP_404_NOT_FOUND
            )

class UserProfileListView(APIView):
    """
    List all user profiles
    """
    # permission_classes = [permissions.IsAdminUser]
    
    @extend_schema(
        summary="List all user profiles",
        responses=UserProfileSerializer(many=True),
    )
    def get(self, request):
        profiles = UserProfile.objects.all()
        serializer = UserProfileSerializer(profiles, many=True)
        return Response(serializer.data)


class UserProfileDetailView(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a user profile
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    
    def get_permissions(self):
        """
        - GET: Allow access to profile owner or admin
        - PUT/PATCH/DELETE: Admin only
        """
        if self.request.method == 'GET':
            return [permissions.IsAuthenticated()]
        return [permissions.IsAdminUser()]
    
    def get_queryset(self):
        # Regular users can only see their own profile
        if self.request.user.is_staff:
            return UserProfile.objects.all()
        return UserProfile.objects.filter(user=self.request.user)