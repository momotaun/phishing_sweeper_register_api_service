from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import(
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)



class UserManager(BaseUserManager):
    
    def create_user(self, 
                    email, 
                    company_name,
                    phone, 
                    password, 
                    **extra_fields):
        if not email:
            raise ValueError('The Email must be set.')
        if not company_name:
            raise ValueError('The Company name must be set.')
        if not phone:
            raise ValueError('The phone must be set.')
        email = self.normalize_email(email)
        user = self.model(
            email=email, 
            company_name=company_name,
            phone=phone,
            **extra_fields
            )
        user.set_password(password)
        user.save()
        return user
        
    def create_superuser(self, 
                         email, 
                         company_name,
                         phone,
                         password, 
                         **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        
        return self.create_user(
            email, 
            company_name,
            phone,
            password, 
            **extra_fields)
        

class Company(AbstractBaseUser, PermissionsMixin):
    username = None
    first_name = None
    last_name = None
    
    email = models.EmailField(verbose_name=("E-mail"), unique=True, max_length=254)
    company_name = models.CharField(verbose_name=("Company name"), null=True, max_length=50)
    phone = models.CharField(verbose_name=("Phone number"), null=True, max_length=10)
    is_verified = models.BooleanField(verbose_name=("Verified"), default=False)
    is_active = models.BooleanField(verbose_name=("Active"), default=False)
    is_staff = models.BooleanField(verbose_name=("Staff"), default=False)
    created_at = models.DateTimeField(verbose_name=("Created at"), auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=("Updated at"), auto_now=True, auto_now_add=False)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'company_name', 
        'phone',
        # 'registration_number', 
        ]
    
    objects = UserManager()
    
    def __str__(self):
        return self.email
    
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return refresh.access_token
        # return {
        #     'refresh': str(refresh),
        #     'access': str(refresh.access_token)
        # }
        

class CompanyProfile(models.Model):
    
    company = models.OneToOneField(Company, related_name='profile', on_delete=models.CASCADE)    
    registration_number = models.CharField(verbose_name=("Registration Number"), unique=True, null=True, max_length=50)
    imap_url = models.CharField(verbose_name=("IMAP URL"), null=True, blank=True, max_length=254)
    created_at = models.DateTimeField(verbose_name=("Created at"), auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=("Updated at"), auto_now=True, auto_now_add=False)
    # region = models.ForeignKey(Regions, verbose_name=("Region"), null=True, blank=True,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.company.company_name}'s Profile"