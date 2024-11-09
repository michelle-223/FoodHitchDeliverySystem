# Generated by Django 5.0.7 on 2024-09-12 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodHitchApp', '0012_alter_rider_options_rider_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rider',
            name='Email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='rider',
            name='Username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
