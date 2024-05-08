from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=255)
    Last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    is_supervisor = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Shop(models.Model):
    shop_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    users = models.ForeignKey(User, related_name="shops",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Brand(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class car_model(models.Model):
    name = models.CharField(max_length=255)
    brands = models.ForeignKey(Brand, related_name="models",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Fuel(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Car_Feature(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Car(models.Model):
    car_seats = models.IntegerField(max_length=2)
    transmition = models.CharField(max_length=255)
    milge = models.IntegerField(max_length=10)
    status = models.BooleanField(default=True)
    price = models.IntegerField()
    Carcol = models.CharField(max_length=255)
    shops = models.ForeignKey(Shop, related_name="cars",on_delete=models.CASCADE)
    fuels = models.OneToOneField(Fuel, related_name="cars",on_delete=models.CASCADE)
    brands = models.OneToOneField(Brand, related_name="cars",on_delete=models.CASCADE)
    car_features = models.ManyToManyField(Car_Feature, related_name="cars")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def add_feature_to_car(request,car_feature_id):
    if request.POST['car_id']:
        thisCar_Feature = Car_Feature.objects.get(id=car_feature_id)
        thisCar = Car.objects.get(id=request.POST['car_id'])
        thisCar_Feature.cars.add(thisCar)

class Reservation(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    users = models.ForeignKey(User, related_name="reservations",on_delete=models.CASCADE)
    cars = models.ForeignKey(Car, related_name="reservations",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



