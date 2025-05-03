from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from drf_spectacular.utils import extend_schema
from .models import UserProfile, CustomUser, EmailVerificationToken
from .serializers import (
    LoginResponseSerializer,
    UserProfileSerializer, 
    CustomUserSerializer,
    UserRegistrationSerializer,
    LoginSerializer,
    OTPVerificationSerializer,
    ResendOTPSerializer
)
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.db import transaction
from .utils import send_verification_email


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
                {
                    "message": "Registration successful. Please check your email for verification code.",
                    "user": UserProfileSerializer(profile).data
                }, 
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
            200: LoginResponseSerializer,
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
                        {
                            "error": "Please verify your email before logging in.",
                            "email_verification_required": True,
                            "email": email
                        },
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
                
                serializer = UserProfileSerializer(user.profile)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'user': serializer.data,
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


class VerifyEmailView(APIView):
    """
    Verify a user's email address using an OTP code
    """
    permission_classes = [permissions.AllowAny]
    
    @extend_schema(
        summary="Verify user email with OTP",
        request=OTPVerificationSerializer,
        responses={
            200: {"description": "Email verified successfully"},
            400: {"description": "Invalid OTP or OTP expired"},
            404: {"description": "OTP not found"}
        },
    )
    def post(self, request):
        serializer = OTPVerificationSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        email = serializer.validated_data['email']
        otp = serializer.validated_data['otp']
        
        
        try:
            # Find and verify the token
            verification_token = EmailVerificationToken.verify_otp(email, otp)
            
            # Mark user as verified
            with transaction.atomic():
                user = verification_token.user
                user.email_verified = True
                user.save()
                
                # Delete the token as it's been used
                verification_token.delete()
                
            
            # Generate auth tokens for automatic login after verification
            refresh = RefreshToken.for_user(user)
            
            try:
                profile = user.profile
                user_type = profile.user_type
                name = f"{profile.first_name} {profile.last_name}"
            except:
                user_type = None
                name = None
            serializer = UserProfileSerializer(user.profile)
            return Response({
                "message": "Email verified successfully. You can now log in.",
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user_profile": serializer.data,
            }, status=status.HTTP_200_OK)
            
        except ValueError as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
        except EmailVerificationToken.DoesNotExist:
            return Response(
                {"error": "Invalid OTP code or email address."},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            # Log the exception for debugging
            print(f"Unexpected verification error: {str(e)}")
            return Response(
                {"error": "An error occurred during verification."},
                status=status.HTTP_400_BAD_REQUEST
            )


class ResendVerificationEmailView(APIView):
    """
    Resend verification OTP to the user
    """
    permission_classes = [permissions.AllowAny]
    
    @extend_schema(
        summary="Resend verification OTP",
        request=ResendOTPSerializer,
        responses={
            200: {"description": "Verification OTP sent"},
            400: {"description": "Invalid email or account already verified"},
            404: {"description": "User not found"}
        },
    )
    def post(self, request):
        serializer = ResendOTPSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        email = serializer.validated_data['email']
        
        try:
            user = CustomUser.objects.get(email=email)
            
            # Check if user is already verified
            if user.email_verified:
                return Response(
                    {"error": "Email is already verified."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Create new token with OTP
            token_obj, otp = EmailVerificationToken.create_for_user(user)
            
            # Send verification email with OTP
            send_verification_email(user, otp)
            
            return Response(
                {"message": "Verification code sent to your email."},
                status=status.HTTP_200_OK
            )
            
        except CustomUser.DoesNotExist:
            # For security reasons, don't reveal whether the email exists
            return Response(
                {"message": "If this email exists in our system, a verification code has been sent."},
                status=status.HTTP_200_OK
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