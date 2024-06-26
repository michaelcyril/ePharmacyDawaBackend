# Generated by Django 5.0.6 on 2024-06-26 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_management', '0012_order_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
        migrations.AddField(
            model_name='ordermedicine',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ordermedicine',
            name='total_amount',
            field=models.IntegerField(default=0),
        ),
    ]
