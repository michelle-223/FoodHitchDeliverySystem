# Generated by Django 5.1.1 on 2024-09-10 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodHitchApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='Password',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Phone',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
