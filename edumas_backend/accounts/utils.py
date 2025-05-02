from django.core.mail import send_mail
from django.conf import settings

def send_verification_email(user, otp):
    """
    Send verification email with OTP to user
    
    Args:
        user: CustomUser instance
        otp: One-time password to send
    """
    subject = 'Verify Your Email - OTP Code'
    message = f"""
    Hello {user.email},
    
    Thank you for registering with our service. To complete your registration, please use the following verification code:
    
    {otp}
    
    This code will expire in 30 minutes.
    
    If you did not request this verification, please ignore this email.
    
    Best regards,
    Your Application Team
    """
    
    from_email = getattr(settings, 'DEFAULT_FROM_EMAIL', 'noreply@example.com')
    recipient_list = [user.email]
    
    # Send email
    send_mail(
        subject=subject,
        message=message,
        from_email=from_email,
        recipient_list=recipient_list,
        fail_silently=False
    )
    
    # Log for debugging
    print(f"Verification email sent to {user.email}")
    print(f"OTP: {otp}")