from rest_framework import serializers
from .models import *


class DeseasePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desease
        fields = [
            'name',
        ]

class DeseaseGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desease
        fields = "__all__"
        depth = 2


class MedicinePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = [
            'name',
            'description',
            'dosage',
            'desease',
            'image',
            'type',
            'price',
        ]

class MedicineGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = "__all__"
        depth = 2


class OrderPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'client',
            'prescription',
            'total_price',
            'description',
        ]

class OrderGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
        depth = 2


class OrderMedicinePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderMedicine
        fields = [
            'medicine',
            'order',
            'dosage',
        ]

class OrderMedicineGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderMedicine
        fields = "__all__"
        depth = 2

