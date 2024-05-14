from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

class UserManager(BaseUserManager):
  #validate email using django built in function   
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