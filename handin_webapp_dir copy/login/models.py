from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

borrower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

class Users(AbstractBaseUser):
    first_name = models.TextField(max_length=100)
    last_name = models.TextField(max_length=100)
    username = models.CharField(max_length=50, unique = "True")
    password = models.TextField(max_length=150)
    email = models.TextField(max_length=150)
 

class NotConfirmedUsers(AbstractBaseUser):
    first_name = models.TextField(max_length=100)
    last_name = models.TextField(max_length=100)
    username = models.CharField(max_length=50, unique = "True")
    password = models.TextField(max_length=150)
    email = models.TextField(max_length=150)
 
