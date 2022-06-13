from django.urls import path
from .views import(
    RegisterAPIView,
    # LoginAPIView,
    # VerifyAPIEmail,
    # CompanyProfileListAPIView,
    # CompanyProfileAPIView,
    # PasswordTokenCheckAPI, 
    # RequestPasswordResetEmail,
    # SetNewPasswordAPIView,
    # LogoutAPIView
)
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    # path('login/', LoginAPIView.as_view(), name='login'),
    # path('logout/', LogoutAPIView.as_view(), name="logout"),
    # path('email-verify/', VerifyAPIEmail.as_view(), name='email-verify'),
    # path('profile/', CompanyProfileListAPIView.as_view(), name="email-users"),
    # path('profile/<int:id>', CompanyProfileAPIView.as_view(), name="email-user"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('request-reset-email/', RequestPasswordResetEmail.as_view(), name="request-reset-email"),
    # path('password-reset/<uidb64>/<token>/', PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    # path('password-reset-complete', SetNewPasswordAPIView.as_view(), name='password-reset-complete'),
]