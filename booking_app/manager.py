from django.db.models import Manager

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
  
class ReservationManager(Manager):
  def create_reservation(self, car, user, start_date, end_date, shop):
    reservation = self.create(users=user, cars = car, start_date = start_date, end_date = end_date, shop=shop)
    reservation.save()
    return reservation

class ShopManager(Manager):
  def get_all_shops(self):
    return self.all()
  
  def get_shop_by_id(self,id):
    shop = self.filter(id=id).first()
    if shop:
      return shop
    return False