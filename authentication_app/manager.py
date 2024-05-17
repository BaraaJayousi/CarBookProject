from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db import models
import bcrypt
import re

class UserManager(BaseUserManager):
  #validate email using django built in function
  def user_validator(self,postData):
        errors={}
        EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z0-9.+_-]+$')
        if len(postData['first_name'])<2:
            errors["first_name"]="first name should be at least 2 characters"
            return errors
        if len(postData['last_name'])<2:
            errors["last_name"]="first name should be at least 2 characters"
            return errors
        if len(postData['phone_number'])<10:
            errors["phone_number"]="first name should be at least 2 characters"
            return errors
        if len(postData['password'])<8:
            errors["password"]="Password should be at least 8 characters"
            return errors
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
            return errors
        conf_field=postData['password']
        if not conf_field.match(postData['conf_pw']):
            errors['conf_pw'] = "password does not matched!"
            return errors
        
  def email_validator(self, email):
    try:
      validate_email(email)
    except ValidationError:
      raise ValueError("Please Enter a valid email address")

#create the user
  def create_user(self, email, first_name, last_name, password, **extra_fields):
    if email:
      email = self.normalize_email(email)
      self.email_validator(email)
    else:
      raise ValueError("An email address is required")

    if not first_name:
      raise ValueError("A first name is required")
    
    if not last_name:
      raise ValueError("A last name is required")
    
    if not password:
      raise ValueError("Required! , The Password should be at lest 8 characters")
    
    user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)
    #a django built in function to hash the password
    user.set_password(password)
    user.save(using=self._db)
    return user
  
  def create_superuser(self, email, first_name, last_name, password, **extra_fields):
    extra_fields.setdefault("is_superuser", True)
    extra_fields.setdefault("is_staff", True)

    if extra_fields.get("is_superuser") is not True:
      raise ValueError("is superuser must be true for admin user")
    
    if extra_fields.get("is_staff") is not True:
      raise ValueError("is staff must be true for admin user")
    
    user = self.create_user(email, first_name, last_name, password, **extra_fields )
    user.save(using=self._db)
    return user