# Generated by Django 5.0.4 on 2024-05-09 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0011_modelyear_carmodel_model_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_image',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
