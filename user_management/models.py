from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = (
        ("ADMIN", "System admin"),
        ("NORMAL", "Normal person"),
    )
    STATUS = (
        ("DELETED", "User deleted"),
        ("ACTIVE", "Active user"),
        ("INACTIVE", "Inactive user"),
    )
    GENDER = (
        ("MALE", "male"),
        ("FEMALE", "female"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=100, unique=True)
    dob = models.DateField(auto_now_add=False, null=True, blank=True)
    phone = models.CharField(max_length=12, unique=True)
    gender = models.CharField(choices=GENDER, null=True, blank=True , max_length=20)
    address = models.CharField(null=True, blank=True , max_length=20)
    profileComplete = models.BooleanField(default=False)
    otp = models.CharField(max_length=10)
    otp_created_at = models.DateTimeField(auto_now_add=True)
    role = models.CharField(choices=ROLE_CHOICES, default='CLIENT', max_length=20)
    status = models.CharField(choices=STATUS, default='INACTIVE', max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'
