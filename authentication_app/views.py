from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from .forms import  RegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

# Create your views here.

class Login(View):
  template = 'login.html'
  context = { "LoginForm": AuthenticationForm()}
  def get(self, request):
    return render(request=request, template_name= self.template, context=self.context)
  
  def post(self,request):
    bound_form = AuthenticationForm(request, data=request.POST)
    if bound_form.is_valid():
      email= bound_form.cleaned_data.get('username')
      password= bound_form.cleaned_data.get('password')
      user= authenticate(request=request, email=email, password=password)
      if user:
        login(request, user)
        messages.info(request, f"You are now logged in as {user}")
        # Return to homepage
        return redirect("booking_app:home_page")
      else:
        messages.error(request,"Invalid username or password.")
    else:
      messages.error(request,"Invalid username or password.")
    return redirect("auth_app:login_form")
  
class Logout(View):
  def post(self, request):
    if request.user.is_authenticated:
      print(request.user)
      logout(request)
      messages.info(request, "You have successfully logged out")
    messages.error(request, "You are not authorized")
    return redirect("booking_app:home_page")
  
  def get(self, request):
    return redirect("booking_app:home_page")

class Register(View):
  template = 'register.html'
  context = {"RegisterForm": RegisterForm()}

  def get(self, request):
    return render(request, self.template, self.context)

  def post(self, request):
    bound_form = RegisterForm(request.POST)
    if bound_form.is_valid():
      user = bound_form.save(commit=False)
      user.save()
      return redirect(reverse("auth_app:login_form"))
    else:
      self.context['registerForm'] = bound_form
      return redirect(reverse("auth_app:register_form"))