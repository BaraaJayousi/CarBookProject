# Generated by Django 5.0.4 on 2024-05-09 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0009_rename_fuel_carmodel_brand_model_alter_car_car_seats_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Car_Feature',
            new_name='CarFeature',
        ),
    ]
