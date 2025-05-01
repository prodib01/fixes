from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_verification_email(user, raw_token):
    """Send verification email to the user."""
    verification_url = f"{settings.FRONTEND_URL}/verify-email/{raw_token}"
    
    subject = "Verify your email address"
    html_message = render_to_string('email/verification_email.html', {
        'user': user,
        'verification_url': verification_url,
        'valid_days': 2  # Match this to the expiration time in the model
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
        html_message=html_message,
        fail_silently=False,
    )