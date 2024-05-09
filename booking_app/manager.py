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