from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from .models import Car, Shop, Reservation
from django.contrib import messages
from datetime import datetime
from .validators import validate_booking_range

class HomePage(View):
  view_template = "index.html"
  context = {}
  def get(self, request):
    self.context['featured_cars'] = Car.objects.get_featured_cars()
    self.context['locations'] = Shop.objects.get_all_shops()
    return render(request, self.view_template, self.context)

class AboutPage(View):
  view_template = "about.html"
  context = {}
  def get(self, request):
    return render(request, self.view_template)

class ServicesPage(View):
  view_template = "services.html"
  context = {}
  def get(self, request):
    return render(request, self.view_template)

class CarsPage(View):
  view_template = "car.html"
  context = {}
  def get(self, request):
    start_date = datetime.fromisoformat(request.GET.get('start_date'))
    end_date = datetime.combine(datetime.fromisoformat(request.GET.get('end_date')),start_date.time())
    valid_date = validate_booking_range(request=request, start_date=start_date, end_date=end_date)
    if valid_date:
      self.context['locations'] = Shop.objects.get_all_shops()
      shop_id =  request.GET.get('location')
      self.context['book_details'] = request.GET
      self.context['cars'] = Car.objects.get_available_cars(start_date, end_date, shop_id) 
      return render(request, self.view_template, self.context)
    return redirect(reverse("booking_app:home_page"))
    
      
  def post(self, request):
    start_date = datetime.fromisoformat(request.POST.get('start_date'))
    end_date = datetime.combine(datetime.fromisoformat(request.POST.get('end_date')),start_date.time())
    valid_date = validate_booking_range(request=request, start_date=start_date, end_date=end_date)
    if valid_date:
      shop_id = request.POST.get('location')
      self.context['book_details'] = request.POST
      self.context['cars'] = Car.objects.get_available_cars(start_date, end_date, shop_id) 
      return render(request, "search-results.html", self.context)
    return render(request, 'messages-template.html', self.context)

class CarDetailsPage(View):
  view_template = "car-single.html"
  context = {}
  def get(self, request, id):
    car = Car.objects.get_car_by_id(id)
    if car:
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


class MyBookings(View):
  view_template = "my-bookings.html"
  context = {}

  def get(self, request):
    if request.user.is_authenticated:
      user_bookings = Reservation.objects.get_reservations_by_user_id(request.user)
      if user_bookings:
        self.context['bookings'] = user_bookings
        return render(request, self.view_template, self.context)
      else:
        messages.error(request, "You don't have any bookings")
    else:
      messages.error(request, "You need to logged in first")
      
    return redirect(reverse("booking_app:home_page"))
  
  # cancels  a pending reservation
  def post(self, request):
    if request.user.is_authenticated:
      got_canceled = Reservation.objects.cancel_pending_reservations_by_id(reservation_id = request.POST.get('booking_id'), user = request.user)
      self.context['bookings'] = Reservation.objects.get_reservations_by_user_id(request.user)
      return render(request, "bookings_table.html", self.context)
      
