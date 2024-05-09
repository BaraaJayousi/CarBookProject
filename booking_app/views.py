from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from .models import Car

class HomePage(View):
  view_template = "index.html"
  context ={}
  def get(self, request):
    self.context['featured_cars'] = Car.objects.get_featured_cars()
    return render(request, self.view_template, self.context)


