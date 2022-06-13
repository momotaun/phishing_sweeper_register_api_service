# import os
# import jwt
# from base64 import urlsafe_b64encode
# from django.contrib.auth.tokens import PasswordResetTokenGenerator
# from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
# from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
# from django.http import HttpResponsePermanentRedirect
from ..management.helpers.utils import Util
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
# from django.contrib.sites.shortcuts import get_current_site
# from django.conf import settings
from django.urls import reverse
# from drf_yasg import openapi
# from drf_yasg.utils import swagger_auto_schema
# from rest_framework import permissions
from ..management.helpers.permissions import IsOwner
from ..management.helpers.renderers import UserRenderer
from ..models import(
    Company, 
    CompanyProfile
    ) 
from .serializers import(
    RegisterUserSerializer,
    # EmailVerificationSerializer,
    # LoginUserSerializer,
    # CompanyProfileSerializer,
    # ResetPasswordEmailRequestSerializer,
    # SetNewPasswordSerializer,
    # LogoutSerializer,
    ) 
from rest_framework import(
    generics,
    status,
    views
    )


class RegisterAPIView(generics.GenericAPIView):
    
    serializer_class = RegisterUserSerializer
    renderer_class = UserRenderer
    
    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data        
        user = Company.objects.get(email=user_data['email'])        
        token = RefreshToken.for_user(user).access_token        
        # current_site = get_current_site(request).domain
        current_site = 'http://localhost:4200'
        relativeLink = reverse('email-verify')
        absolut_url = current_site+relativeLink+"?token="+str(token)
        email_body = "Hello, "+ user.company_name+"\n\nTo verify your email address and finish setting up your account, use the link below:\n"+absolut_url+"\n\nIf you did not sign up for an account with Con-Act Smart E-mail Filtering, you can disregard this email.\n\nGlad to you chose to be secure!\nCon-Act Crew"
        data = {'email_body': email_body, 'email_to': user.email, 'email_subject': 'Please Confirm Your E-mail Address'}
        
        Util.send_email(data)
        
        return Response(user_data, status=status.HTTP_201_CREATED)