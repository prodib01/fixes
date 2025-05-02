from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.db import transaction
from .models import UserProfile, EmailVerificationToken
from .utils import send_verification_email

User = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'email_verified', 'is_active', 'date_joined')
        read_only_fields = ('email_verified', 'is_active', 'date_joined')
        extra_kwargs = {'password': {'write_only': True}}


class UserProfileSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    class Meta:
        model = UserProfile
        fields = (
            'id', 'user', 'user_type', 'gender', 'first_name', 'last_name', 
            'other_name', 'dob', 'phone', 'profile_picture', 
            'emergency_contact', 'emergency_phone'
        )
        read_only_fields = ('id', 'email')


class UserRegistrationSerializer(serializers.Serializer):
    # User fields
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    
    # Profile fields
    user_type = serializers.ChoiceField(choices=UserProfile.USER_TYPE_CHOICES, required=False)
    gender = serializers.ChoiceField(choices=UserProfile.GENDER_CHOICES, required=False, allow_null=True)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    other_name = serializers.CharField(max_length=100, required=False, allow_blank=True, allow_null=True)
    dob = serializers.DateField(required=False, allow_null=True)
    phone = serializers.CharField(max_length=20, required=False, allow_blank=True, allow_null=True)
    emergency_contact = serializers.CharField(max_length=100, required=False, allow_blank=True, allow_null=True)
    emergency_phone = serializers.CharField(max_length=20, required=False, allow_blank=True, allow_null=True)
    
    def validate_email(self, value):
        """Check that the email is not already in use"""
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value
    

    
    @transaction.atomic
    def create(self, validated_data):

        # Extract user fields and profile fields
        user_data = {
            'email': validated_data.pop('email'),
            'password': validated_data.pop('password'),
            'email_verified': False,  # User needs to verify email
            'is_active': True,  # User can log in but with limited access
        }
        
        # Create user
        user = User.objects.create_user(**user_data)
        
        # Create profile linked to the user
        profile = UserProfile.objects.create(user=user, **validated_data)
        
        # Generate OTP verification token
        token_obj, otp = EmailVerificationToken.create_for_user(user)
        
        # Send verification email with OTP
        send_verification_email(user, otp)
        
        return profile


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})


class OTPVerificationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6, min_length=6)
    
    def validate_otp(self, value):
        """Check that OTP is numeric"""
        if not value.isdigit():
            raise serializers.ValidationError("OTP must contain only digits.")
        return value
    
    def validate(self, data):
        """Validate the OTP for the given email"""
        email = data.get('email')
        otp = data.get('otp')
        
        # Let the view handle the actual verification logic
        # This is just basic validation
        
        return data


class ResendOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()