# Generated by Django 5.0.6 on 2024-06-21 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_management', '0003_medicine_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='dosage',
            field=models.CharField(default=1, max_length=225),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('PROCESSING', 'Processing'), ('DELIVERED', 'Delivered')], default='PENDING', max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
