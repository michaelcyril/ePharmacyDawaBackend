# Generated by Django 5.0.6 on 2024-06-22 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_management', '0006_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='type',
            field=models.CharField(choices=[('OTC', 'Otc'), ('DESEASE', 'Desease')], default='DESEASE', max_length=20),
        ),
    ]