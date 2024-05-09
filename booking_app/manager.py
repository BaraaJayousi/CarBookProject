from django.db.models import Manager

class CarManager(Manager):
  def get_featured_cars(self):
    return self.filter(featured=True)