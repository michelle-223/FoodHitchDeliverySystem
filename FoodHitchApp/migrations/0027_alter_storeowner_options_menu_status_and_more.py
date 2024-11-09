# Generated by Django 5.0.7 on 2024-09-22 23:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodHitchApp', '0026_alter_storeowner_options_storeowner_hasbir203'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='storeowner',
            options={'verbose_name_plural': 'Store Owners'},
        ),
        migrations.AddField(
            model_name='menu',
            name='Status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=10),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='OwnerID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FoodHitchApp.storeowner'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='Status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=10),
        ),
    ]
