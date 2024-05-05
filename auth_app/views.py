from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View

# Create your views here.

class Login(View):
  template = 'login.html'
  context = { }
  def get(self, request):
    return render(request=request, template_name= self.template, context=self.context)
  
class Register(View):
  template = 'register.html'
  context = {}
  def get(self, request):
    return render(request, self.template, self.context)
