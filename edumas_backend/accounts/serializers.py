from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser, UserProfile, EmailVerificationToken
from .utils import send_verification_email


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source='user.email', read_only=True)
    
    class Meta:
        model = UserProfile
        fields = [
            'id', 'user', 'user_email', 'user_type', 'first_name', 'last_name',
            'other_name', 'gender', 'dob', 'phone', 'profile_picture',
            'emergency_contact', 'emergency_phone'
        ]


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})
    
    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        
        if email and password:
            return data
        raise serializers.ValidationError("Must include 'email' and 'password'.")


class UserRegistrationSerializer(serializers.Serializer):
    # User fields
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    
    # Profile fields
    user_type = serializers.ChoiceField(
        choices=UserProfile.USER_TYPE_CHOICES,
        default='student'
    )
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    other_name = serializers.CharField(required=False, allow_blank=True)
    gender = serializers.ChoiceField(
        choices=UserProfile.GENDER_CHOICES,
        required=False,
        allow_null=True
    )
    dob = serializers.DateField(required=False, allow_null=True)
    phone = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    
    def create(self, validated_data):
        # Extract user data
        user_data = {
            'email': validated_data.pop('email'),
            'password': validated_data.pop('password'),
            'is_active': False,  # Set to False until email verification
        }
        
        # Create user
        user = CustomUser.objects.create_user(**user_data)
        
        # Create profile
        profile = UserProfile.objects.create(user=user, **validated_data)
        
        token = EmailVerificationToken.objects.create(user=user)
        
        # Send verification email
        self.send_verification_email(user, token)
        
        return profile
    
    def send_verification_email(self, user, token):
        # This will be implemented in the email sending utility
        send_verification_email(user, token)