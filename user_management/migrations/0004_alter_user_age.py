# Generated by Django 5.0.6 on 2024-05-15 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0003_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]