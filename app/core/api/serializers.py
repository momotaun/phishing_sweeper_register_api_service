from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from django.contrib import auth
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from ..models import(
    Company,
    CompanyProfile,
    )


class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=254, min_length=6, write_only=True)
    company_name = serializers.CharField(max_length=50, required=True, write_only=True)
    phone = serializers.CharField(max_length=10, required=True, write_only=True)
    
    class Meta:
        model = Company
        fields = [
            'id',
            'email',
            'company_name', 
            'phone',
            'password'
            ]
        
    def validate(self, attrs):
        email = attrs.get('email', '')
        
        return attrs
    
    def create(self, validated_data):
        return Company.objects.create_user(**validated_data)