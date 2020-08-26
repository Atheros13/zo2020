from __future__ import unicode_literals

from django.db import models
from django.conf import settings 
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail, BadHeaderError
from django.utils.translation import ugettext_lazy as _

from django.db.models import Q
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class UserManager(BaseUserManager):
    
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):

    '''

    

    '''
    is_staff = models.BooleanField(default=False) 

    email = models.EmailField(unique=True)

    is_active = models.BooleanField(default=True)

    temporary_password = models.CharField(max_length=50, blank=True)  
    is_verified = models.BooleanField(default=False) 

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    ### META DATA ###
    class Meta:

        verbose_name = 'user'
        verbose_name_plural = 'users'
        
    def __str__(self):

        ''' '''

        return self.email


