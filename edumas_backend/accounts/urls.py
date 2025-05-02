from django.urls import path
from .views import (
    UserRegistrationView,
    UserProfileListView,
    UserProfileDetailView,
    LoginView,
    LogoutView,
    VerifyEmailView,
    ResendVerificationEmailView
)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profiles/', UserProfileListView.as_view(), name='profile-list'),
    path('profiles/<int:pk>/', UserProfileDetailView.as_view(), name='profile-detail'),
    path('verify-email/', VerifyEmailView.as_view(), name='verify-email'),
    path('resend-verification/', ResendVerificationEmailView.as_view(), name='resend-verification'),
]