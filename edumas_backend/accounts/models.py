from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.utils import timezone
import uuid
from datetime import timedelta
import hashlib
import random



class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)
    email_verified = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"

class EmailVerificationToken(models.Model):
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE, related_name='verification_token')
    otp = models.CharField(max_length=6, editable=False)  # Store the 6-digit OTP
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    
    def save(self, *args, **kwargs):
        # Set expiration date if not already set
        if not self.expires_at:
            self.expires_at = timezone.now() + timedelta(minutes=30)
        super().save(*args, **kwargs)
    
    def is_valid(self):
        return timezone.now() <= self.expires_at
    
    @classmethod
    def create_for_user(cls, user):
        """
        Create a new verification OTP for the given user.
        
        Returns:
        - token_obj: The saved token object
        - otp: The generated OTP code
        """
        # Delete any existing tokens for this user
        cls.objects.filter(user=user).delete()
        
        # Generate a 6-digit OTP
        otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        
        # Create and save the token object
        token_obj = cls.objects.create(
            user=user,
            otp=otp,
            expires_at=timezone.now() + timedelta(minutes=30)
        )
        
        # Log token creation for debugging
        print(f"Created OTP for {user.email}:")
        print(f"- OTP: {otp}")
        print(f"- Record ID: {token_obj.id}")
        
        return token_obj, otp
    
    @classmethod
    def verify_otp(cls, email, otp):
        """
        Verify an OTP code for a specific user email.
        
        Args:
        - email: The user's email address
        - otp: The OTP code to verify
        
        Returns:
        - The EmailVerificationToken instance if valid
        
        Raises:
        - EmailVerificationToken.DoesNotExist: If the token is not found
        - ValueError: If OTP is invalid or expired
        """
        try:
            # Find the token by the user's email
            token_obj = cls.objects.select_related('user').get(user__email=email, otp=otp)
            
            if not token_obj.is_valid():
                raise ValueError("OTP has expired")
                
            print(f"- Verified OTP for user: {token_obj.user.email}")
            return token_obj
        except cls.DoesNotExist:
            print(f"No valid OTP found for email: {email}")
            raise
        
    def __str__(self):
        return f"Verification OTP for {self.user.email}"
    
    @classmethod
    def verify_otp(cls, email, otp):
        """
        Verify an OTP code for a specific user email.
        
        Args:
        - email: The user's email address
        - otp: The OTP code to verify
        
        Returns:
        - The EmailVerificationToken instance if valid
        
        Raises:
        - EmailVerificationToken.DoesNotExist: If the token is not found
        - ValueError: If OTP is invalid or expired
        """
        try:
            # Find the token by the user's email
            token_obj = cls.objects.select_related('user').get(user__email=email, otp=otp)
            
            if not token_obj.is_valid():
                raise ValueError("OTP has expired")
                
            print(f"- Verified OTP for user: {token_obj.user.email}")
            return token_obj
        except cls.DoesNotExist:
            print(f"No valid OTP found for email: {email}")
            raise
        
    def __str__(self):
        return f"Verification token for {self.user.email}"


class UserProfile(models.Model):
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    )
    USER_TYPE_CHOICES = (
        ("admin", "Admin"),
        ("school_owner", "School Owner"),
        ("staff", "Staff"),
        ("student", "Student"),
        ("parent", "Parent"),
    )
    user_type = models.CharField(
        max_length=20, choices=USER_TYPE_CHOICES, default="school_owner"
    )
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="profile",
        blank=True,
        null=True,
    )
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, blank=True, null=True
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    other_name = models.CharField(max_length=100, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profiles/", blank=True, null=True)
    emergency_contact = models.CharField(max_length=100, blank=True, null=True)
    emergency_phone = models.CharField(max_length=20, blank=True, null=True)
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_full_name(self):
        full_name = f"{self.first_name} {self.last_name}"
        if self.other_name:
            full_name = f"{full_name} {self.other_name}"
        return full_name

    def get_short_name(self):
        return self.first_name


class Role(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    school = models.ForeignKey(
        "core.School",
        on_delete=models.CASCADE,
        related_name="roles",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name


class PermissionCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Permission(models.Model):
    category = models.ForeignKey(
        PermissionCategory, on_delete=models.CASCADE, related_name="permissions"
    )
    code = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class RolePermission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="permissions")
    permission = models.ForeignKey(
        Permission, on_delete=models.CASCADE, related_name="roles"
    )

    class Meta:
        unique_together = ["role", "permission"]

    def __str__(self):
        return f"{self.role} - {self.permission}"


class StaffRole(models.Model):
    staff = models.ForeignKey(
        "academics.Staff", on_delete=models.CASCADE, related_name="staff_roles"
    )
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="staff_roles")

    class Meta:
        unique_together = ["staff", "role"]

    def __str__(self):
        return f"{self.staff} - {self.role}"


class UserPermission(models.Model):
    user = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="user_permissions"
    )
    permission = models.ForeignKey(
        Permission, on_delete=models.CASCADE, related_name="user_permissions"
    )

    class Meta:
        unique_together = ["user", "permission"]

    def __str__(self):
        return f"{self.user} - {self.permission}"


class Document(models.Model):
    profile = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="documents"
    )
    name = models.CharField(max_length=100)
    doc = models.FileField(upload_to="documents/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
