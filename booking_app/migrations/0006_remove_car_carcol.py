# Generated by Django 5.0.4 on 2024-05-09 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0005_rename_brands_car_brand_rename_fuels_car_fuel_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='Carcol',
        ),
    ]