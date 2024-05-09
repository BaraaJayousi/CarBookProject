# Generated by Django 5.0.4 on 2024-05-09 07:35

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0010_rename_car_feature_carfeature'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=4)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='carmodel',
            name='model_year',
            field=models.ForeignKey(default="", on_delete=django.db.models.deletion.CASCADE, to='booking_app.modelyear'),
            preserve_default=False,
        ),
    ]
