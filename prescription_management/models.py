from django.db import models
from user_management.models import User
import uuid

class Prescription(models.Model):
    STATUS = (
        ("DELETED", "User deleted"),
        ("ACTIVE", "Active user"),
        ("INACTIVE", "Inactive user"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # image = models.ImageField()
    status = models.CharField(choices=STATUS, default='INACTIVE', max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.status}'

    class Meta:
        db_table = 'prescription'
