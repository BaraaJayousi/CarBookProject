from django.db.models import Manager
from django.db.models import Q

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
  
  def cancel_pending_reservations_by_id(self, user, reservation_id):
    reservation = self.filter(users = user, id= reservation_id).first()
    if reservation and reservation.status == "Pending":
      reservation.status = "Canceled"
      reservation.save()
      return True
    return False


class ShopManager(Manager):
  def get_all_shops(self):
    return self.all()
  
  def get_shop_by_id(self,id):
    shop = self.filter(id=id).first()
    if shop:
      return shop
    return False