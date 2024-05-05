from django import forms
from .models import User

class LoginForm(forms.ModelForm):
  class Meta:
    model= User
    fields = ['email','password']
    widgets= {
      'password': forms.PasswordInput()
    }


class RegisterForm(forms.ModelForm):
  confirmPwd = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput(), label= "Confirm Password")
  class Meta:
    model= User
    fields = ['first_name', 'last_name', 'email', 'phone_number', 'password', 'confirmPwd']
    widgets= {
      'password': forms.PasswordInput()
    }
  
  def save(self, commit=True):
    user = User.objects.create_user(email= self.cleaned_data['email'], first_name = self.cleaned_data['first_name'], last_name = self.cleaned_data['last_name'], phone_number= self.cleaned_data['phone_number'], password = self.cleaned_data['password'])

    if commit:
      user.save()

    return user