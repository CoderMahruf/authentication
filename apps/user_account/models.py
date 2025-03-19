from django.db import models
from django.contrib.auth.models import PermissionsMixin,AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from  apps.user_account.managers import UserManager
# Create your models here.

class User(AbstractBaseUser,PermissionsMixin):
    USER = 1
    SUPERUSER = 2
    ROLE_CHOICE = (
        (USER, 'User'),
        (SUPERUSER, 'Superuser')
    )
    username = models.CharField(max_length=50,unique=True,validators=[UnicodeUsernameValidator()])
    email = models.EmailField(max_length=50,unique=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICE,default=USER)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    objects = UserManager()
    
    def __str__(self):
        return self.username

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        ordering = ["-date_joined"]

    def save(self,*args,**kwargs):
        if self.is_superuser:
            self.role = 2 
        super().save(*args, **kwargs)
