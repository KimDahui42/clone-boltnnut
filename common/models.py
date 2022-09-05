from django.db import models
from django.contrib.auth.models import (BaseUserManager,AbstractBaseUser,PermissionsMixin)
from django.core.validators import RegexValidator
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self,email,name,company,userType,phone,jobPosition,password=None):
        if not email:
            raise ValueError('이메일을 입력하세요.')
        user=self.model(
            company=company,
            email=self.normalize_email(email),
            name=name,
            userType=userType,
            phone=phone,
            jobPosition=jobPosition,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,password,name,company,userType,phone,jobPosition):
        user=self.create_user(
            email=self.normalize_email(email),
            password=password,
            name=name,
            company=company,
            userType=userType,
            phone=phone,
            jobPosition=jobPosition,
        )
        user.is_admin=True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    id=models.AutoField(primary_key=True)
    email=models.EmailField(
        verbose_name='email address',
        max_length=300,
        unique=True
    ) #username field
    company=models.CharField(
        verbose_name='company name',
        max_length=50
    )
    joined=models.DateTimeField(
        verbose_name='account created',
        default=timezone.now
    )
    name=models.CharField(
        verbose_name='name',
        max_length=20
    )
    userType=models.CharField(
        verbose_name='user type',
        max_length=30
    )#client/company
    phoneRegex=RegexValidator(regex=r'^([0-9]{9,11})$')
    phone=models.CharField(
        verbose_name='phone number',
        validators=[phoneRegex],max_length=11,unique=True
    )
    jobPosition=models.CharField(
        verbose_name='job position',
        max_length=50
    )
    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
        
    objects=CustomUserManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name','company','userType','phone','jobPosition']

