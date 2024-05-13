from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from .models import Car, Shop, Reservation
from django.contrib import messages
from datetime import datetime

class HomePage(View):
  view_template = "index.html"
  context = {}
  def get(self, request):
    self.context['featured_cars'] = Car.objects.get_featured_cars()
    self.context['locations'] = Shop.objects.get_all_shops()
    return render(request, self.view_template, self.context)
  

class CarsPage(View):
  view_template = "car.html"
  context = {}
  def get(self, request):
    start_date = datetime.fromisoformat(request.GET.get('start_date'))
    end_date = datetime.combine(datetime.fromisoformat(request.GET.get('end_date')),start_date.time())
    self.context['locations'] = Shop.objects.get_all_shops()
    shop_id =  request.GET.get('location')
    self.context['book_details'] = request.GET
    self.context['cars'] = Car.objects.get_available_cars(start_date, end_date, shop_id) 
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
      car = Car.objects.get_car_by_id(request.GET.get("car_id"))
      start_date = datetime.fromisoformat(request.GET.get('start_date'))
      end_date = datetime.combine(datetime.fromisoformat(request.GET.get('end_date')),start_date.time())
      book_duration = abs((end_date - start_date).days)
      total = book_duration * car.price
      shop_id = request.GET.get('location')
      self.context['location'] = Shop.objects.get_shop_by_id(shop_id)
      self.context['car'] = car
      self.context['book_duration'] = book_duration
      self.context['total'] = total
      self.context['start_date'] = start_date
      self.context['end_date'] = end_date

      return render(request, self.view_template, self.context)
    messages.error(request, "You need to be logged in first")
    return redirect(reverse("booking_app:home_page"))
  
  def post(self, request):
    if request.user.is_authenticated:
      booking = Reservation.objects.create_reservation(car=self.context['car'], user= request.user, start_date=self.context['start_date'], end_date=self.context['end_date'], shop=self.context['location'])
      messages.success(request, "You car is reserved now, wait for confirmation")
      return redirect(reverse("booking_app:home_page"))
    messages.error(request, "You need to be logged in first")
    return redirect(reverse("booking_app:home_page"))

