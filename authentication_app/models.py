from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import UserManager
# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
  email= models.EmailField(max_length=255, unique=True)
  first_name= models.CharField(max_length=255)
  last_name= models.CharField(max_length=255)
  phone_number = models.CharField(max_length=15, unique=True)
  is_superuser= models.BooleanField(default=False)
  is_staff = models.BooleanField(default=False)
  last_login=models.DateTimeField(auto_now=True)
  created_at= models.DateTimeField(auto_now_add=True)
  updated_at= models.DateTimeField(auto_now=True)

  USERNAME_FIELD= 'email'

  REQUIRED_FIELDS= ['first_name', 'last_name']

  objects= UserManager()
  def __str__(self):
    return f"{self.first_name} {self.last_name}"