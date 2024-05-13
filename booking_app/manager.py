from django.db.models import Manager
from django.db.models import Q
from django.db import models
import bcrypt
import re
class UserManager(models.Manager):
    def user_validator(self,postData):
        errors={}
        EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z0-9.+_-]+$')
        if len(postData['fname'])<2:
            errors["fname"]="first name should be at least 2 characters"
            return errors
        if len(postData['lname'])<2:
            errors["lname"]="first name should be at least 2 characters"
            return errors
        if len(postData['password'])<2:
            errors["password"]="Password should be at least 8 characters"
            return errors
        if not EMAIL_REGEX.match(postData['user_email']):
            errors['user_email'] = "Invalid email address!"
            return errors
        conf_field=postData['password']
        if not conf_field.match(postData['conf_pw']):
            errors['conf_pw'] = "password does not matched!"
            return errors

class CarManager(Manager):
  def get_featured_cars(self):
    return self.filter(featured=True)
  
  def get_all_cars(self):
    return self.all()
  
  def get_car_by_id(self, id):
    car = self.filter(id=id).first()
    if car:
      return car
    return False
  
  def get_available_cars(self, start_date, end_date, shop_id):
    # gets all cars without confirmed reservation
    not_approved_cars = self.filter(reservations__isnull=False, shop__id = shop_id).exclude(reservations__status = "Approved")
    not_reserved_cars = self.filter(reservations__isnull=True, shop__id=shop_id)
    # gets cars with reservation outside the required date range
    available_approved_cars = self.filter(reservations__status="Approved", shop__id = shop_id).filter((Q(reservations__start_date__gt = end_date) & Q(reservations__end_date__gt = start_date)) | (Q(reservations__start_date__lt = end_date) & Q(reservations__end_date__lt = start_date)))

    available_cars = not_approved_cars.union(not_reserved_cars, available_approved_cars)
    return available_cars
  
class ReservationManager(Manager):
  def create_reservation(self, car, user, start_date, end_date, shop):
    reservation = self.create(users=user, cars = car, start_date = start_date, end_date = end_date, shop=shop)
    reservation.save()
    return reservation
  
  def get_reservations_by_user_id(self,user):
    reservations = self.filter(users=user)
    if reservations:
      return reservations
    return False


class ShopManager(Manager):
  def get_all_shops(self):
    return self.all()
  
  def get_shop_by_id(self,id):
    shop = self.filter(id=id).first()
    if shop:
      return shop
    return False