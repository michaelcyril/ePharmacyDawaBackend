from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Desease)
admin.site.register(Medicine)
admin.site.register(Order)
admin.site.register(OrderMedicine)