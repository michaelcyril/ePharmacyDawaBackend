# Generated by Django 5.0.6 on 2024-06-22 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_management', '0004_medicine_dosage_order_status_alter_order_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermedicine',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]