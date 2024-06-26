# Generated by Django 5.0.4 on 2024-05-08 18:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Car_Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fuel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('Last_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('is_supervisor', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='car_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('brands', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='models', to='booking_app.brand')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_seats', models.IntegerField(max_length=2)),
                ('transmition', models.CharField(max_length=255)),
                ('milge', models.IntegerField(max_length=10)),
                ('status', models.BooleanField(default=True)),
                ('price', models.IntegerField()),
                ('Carcol', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('brands', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='booking_app.brand')),
                ('car_features', models.ManyToManyField(related_name='cars', to='booking_app.car_feature')),
                ('fuels', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='booking_app.fuel')),
                ('shops', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='booking_app.shop')),
            ],
        ),
        migrations.AddField(
            model_name='shop',
            name='users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shops', to='booking_app.user'),
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cars', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='booking_app.car')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='booking_app.user')),
            ],
        ),
    ]
