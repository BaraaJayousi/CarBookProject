from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from .models import Car
from django.contrib import messages

class HomePage(View):
  view_template = "index.html"
  context = {}
  def get(self, request):
    self.context['featured_cars'] = Car.objects.get_featured_cars()
    return render(request, self.view_template, self.context)
  

class CarsPage(View):
  view_template = "car.html"
  context = {}
  def get(self, request):
    self.context['cars'] = Car.objects.get_all_cars()
    return render(request, self.view_template, self.context)
  

class CarDetailsPage(View):
  view_template = "car-single.html"
  context = {}
  def get(self, request, id):
    car = Car.objects.get_car_by_id(id)
    if car:
      print(car)
      self.context['car'] = car
      return render(request, self.view_template, self.context)
    return redirect(reverse("booking_app:cars_page"))

class CarBookPage(View):
  view_template = "booking-page.html"
  context = {}

  def get(self, request):
    if request.user.is_authenticated:
      return render(request, self.view_template, self.context)
    messages.error(request, "You need to be logged in first")
    return redirect(reverse("booking_app:home_page"))

