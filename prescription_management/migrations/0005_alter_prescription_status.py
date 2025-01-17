# Generated by Django 5.0.6 on 2024-06-23 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prescription_management', '0004_alter_prescription_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('COMPLETE', 'Complete'), ('CANCELED', 'Canceled')], default='INACTIVE', max_length=20),
        ),
    ]
