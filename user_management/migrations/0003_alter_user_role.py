# Generated by Django 5.0.6 on 2024-05-15 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0002_remove_user_dob_user_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('ADMIN', 'System admin'), ('NORMAL', 'Normal person')], default='NORMAL', max_length=20),
        ),
    ]
