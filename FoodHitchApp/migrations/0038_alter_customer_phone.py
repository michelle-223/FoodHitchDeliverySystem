# Generated by Django 5.0.7 on 2024-10-01 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodHitchApp', '0037_remove_customer_password_alter_customer_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Phone',
            field=models.CharField(max_length=15),
        ),
    ]