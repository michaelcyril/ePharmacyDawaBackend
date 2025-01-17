from django.db import models
from user_management.models import User
from prescription_management.models import Prescription
import uuid


class Desease(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'desease'



class Medicine(models.Model):
    TYPE = (
        ("OTC", "Otc"),
        ("DESEASE", "Desease"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)
    dosage = models.CharField(max_length=225)
    desease = models.ForeignKey(Desease, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to="uploads/medicines/", null=True, blank=True)
    type = models.CharField(choices=TYPE, default='DESEASE', max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'medicine'



class Order(models.Model):
    STATUS = (
        ("PENDING", "Pending"),
        ("COMPLETE", "Complete"),
        ("CANCELED", "Canceled"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_id = models.CharField(max_length=20, default="ORDER12212122")
    status = models.CharField(max_length=20, default="PENDING", choices=STATUS)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f''

    class Meta:
        db_table = 'order'



class OrderMedicine(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    medicine = models.ForeignKey(Medicine, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0)
    total_amount = models.IntegerField(default=0)
    dosage = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f''

    class Meta:
        db_table = 'order_medicine'