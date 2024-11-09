# Generated by Django 5.0.7 on 2024-09-17 00:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodHitchApp', '0020_alter_delivery_deliverystatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='RestaurantID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='FoodHitchApp.restaurant'),
        ),
    ]
