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


class OrderPostSerializer(serializers.ModelSerializer):
    order_medicine = OrderMedicinePostSerializer(many=True)
    class Meta:
        model = Order
        fields = [
            'client',
            'prescription',
            'total_price',
            'description',
            'order_medicine',
        ]
    def create(self, validated_data):
        order_medicine = validated_data.pop('order_medicine')
        order = Order.objects.create(**validated_data)
        for medicine in order_medicine:
            OrderMedicine.objects.create(order=order, **medicine)
        return order

class OrderGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
        depth = 2

