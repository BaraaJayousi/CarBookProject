from django.db import models
from authentication_app.models import User
from .manager import CarManager, ReservationManager, ShopManager, UserManager

class Shop(models.Model):
    shop_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name="shops",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ShopManager()
    def __str__(self):
        return f"{self.shop_name} - {self.city}"

class ModelYear(models.Model):
    year = models.CharField(max_length=4)
    created_at = models.DateField( auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.year


class Brand(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.name}"

class CarModel(models.Model):
    name = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.brand} {self.name}"

class CarFeature(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Car(models.Model):
    class TransmissionTypes(models.TextChoices):
        AUTOMATIC = "Automatic"
        MANUAL = "Manual"
    class FuelTypes(models.TextChoices):
        ELECTRIC = "Electric"
        GASOLINE = "Gasoline"
        DIESEL= "Diesel"
        HYBRID = "Hybrid"

    car_seats = models.IntegerField(default=5)
    transmission = models.CharField(max_length=10, default=TransmissionTypes.AUTOMATIC, choices=TransmissionTypes)
    milage = models.IntegerField()
    price = models.IntegerField()
    shop = models.ForeignKey(Shop, related_name="cars",on_delete=models.CASCADE)
    fuel = models.CharField(default=FuelTypes.GASOLINE, choices=FuelTypes, max_length=10)
    model_year = models.ForeignKey(ModelYear, on_delete=models.CASCADE)
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    car_features = models.ManyToManyField(CarFeature, related_name="cars")
    car_image = models.ImageField()
    description = models.TextField(default="Your Description here")
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CarManager()
    def __str__(self):
        return f"{self.car_model} ({self.model_year})"

    # def add_feature_to_car(request,car_feature_id):
    #     if request.POST['car_id']:
    #         thisCar_Feature = CarFeature.objects.get(id=car_feature_id)
    #         thisCar = Car.objects.get(id=request.POST['car_id'])
    #         thisCar_Feature.cars.add(thisCar)


class Reservation(models.Model):
    class ReservationStatus(models.TextChoices):
        APPROVED = "Approved"
        PENDING = "Pending"
        CANCELED = "Canceled"
        DONE = "Done"
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    users = models.ForeignKey(User, related_name="reservations",on_delete=models.CASCADE)
    cars = models.ForeignKey(Car, related_name="reservations",on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, related_name="reservations", on_delete=models.CASCADE)
    status = models.CharField(default=ReservationStatus.PENDING, choices=ReservationStatus, max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects= ReservationManager()



