# Generated by Django 5.0.6 on 2024-06-17 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_management', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
