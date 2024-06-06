from rest_framework import serializers
from .models import *


class PrescriptionPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = [
            'user',
            'image',
        ]

class PrescriptionGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = "__all__"
        depth = 2

