# Generated by Django 5.0.6 on 2024-06-26 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_management', '0011_remove_order_prescription_order_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
