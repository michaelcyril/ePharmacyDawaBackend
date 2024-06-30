from django.db import models
from user_management.models import User
import uuid

class Prescription(models.Model):
    STATUS = (
        ("PENDING", "Pending"),
        ("COMPLETE", "Complete"),
        ("CANCELED", "Canceled"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="uploads/prescription/", null=True, blank=True)
    status = models.CharField(choices=STATUS, default='PENDING', max_length=20)
    prescription_id = models.CharField( default='PRESC1262626', max_length=20)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.status}'

    class Meta:
        db_table = 'prescription'
