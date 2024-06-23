# Generated by Django 5.0.6 on 2024-06-22 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prescription_management', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='status',
            field=models.CharField(choices=[('ACTIVE', 'Active prescription'), ('INACTIVE', 'Inactive prescription')], default='INACTIVE', max_length=20),
        ),
    ]