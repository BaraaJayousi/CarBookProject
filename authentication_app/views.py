from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from .forms import LoginForm, RegisterForm

# Create your views here.

class Login(View):
  template = 'login.html'
  context = { "LoginForm": LoginForm()}
  def get(self, request):
    return render(request=request, template_name= self.template, context=self.context)
  
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