from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
  list_display = ['shop_name', 'user']

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
  list_display = ['brand', 'shop']

@admin.register(Brand)
class CarBrandAdmin(admin.ModelAdmin):
  list_display = ['name']

@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
  list_display = ['name']

@admin.register(ModelYear)
class CarModelYearAdmin(admin.ModelAdmin):
  list_display = ['year']

@admin.register(CarFeature)
class CarFeaturesAdmin(admin.ModelAdmin):
  list_display = ['name']