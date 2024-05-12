from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from .serializer import *
from .models import *
from user_management.models import User
from django.db.models import Q


class CreateGetDeseaseView(APIView):
    permission_classes = [IsAuthenticated, ]
    model = Desease
    post_serializer_class = DeseasePostSerializer
    get_serializer_class = DeseaseGetSerializer
    user_model = User

    def post(self, request):
        data = request.data
        serialized = self.post_serializer_class(data=data)
        if serialized.is_valid():
            serialized.save()
            return Response({"save": True})
        return Response({"save": False})

    def get(self, request):
        queryset = self.model.objects.all()
        serialized = self.get_serializer_class(instance=queryset, many=True)
        return Response(serialized.data)


class UpdateDeleteDeseaseView(APIView):
    model = Desease
    def post(self, request):
        data = request.data
        try:
            desease = self.model.get(id=data['id'])
            desease.name = data['name']
            desease.active = data['active']
            desease.save()
            return Response({"success": True})
        except self.model.DoesNotExist:
            return Response({"success": False})

    def get(self, request):
        try:
            id = request.GET.get("id")
            desease = self.model.get(id=id)
            desease.delete()
            return Response({"delete": True})
        except self.model.DoesNotExist:
            return Response({"delete": False})


class CreateGetMedicineView(APIView):
    permission_classes = [IsAuthenticated, ]
    model = Medicine
    post_serializer_class = MedicinePostSerializer
    get_serializer_class = MedicineGetSerializer
    user_model = Desease

    def post(self, request):
        data = request.data
        serialized = self.post_serializer_class(data=data)
        if serialized.is_valid():
            serialized.save()
            return Response({"save": True})
        return Response({"save": False})

    def get(self, request):
        t = request.GET.get("t")
        q = request.GET.get("q")
        if q == "single":
            d = request.GET.get("d")
            try:
                desease = Desease.objects.get(id=d)
                queryset = self.model.objects.filter(Q(desease=desease)&Q(type=t))
                serialized = self.get_serializer_class(instance=queryset, many=True)
                return Response(serialized.data)
            except Desease.DoesNotExist:
                return Response([])
        elif q == "all":
            desease = Desease.objects.get(id=d)
            queryset = self.model.objects.filter(Q(type=t))
            serialized = self.get_serializer_class(instance=queryset, many=True)
            return Response(serialized.data)
        else:
            return Response([])


class UpdateDeleteMedicineView(APIView):
    model = Medicine
    def post(self, request):
        data = request.data
        try:
            medicine = self.model.get(id=data['id'])
            medicine.name = data['name']
            medicine.desease = data['desease']
            medicine.type = data['type']
            medicine.price = data['price']
            medicine.save()
            return Response({"success": True})
        except self.model.DoesNotExist:
            return Response({"success": False})

    def get(self, request):
        try:
            id = request.GET.get("id")
            medicine = self.model.objects.get(id=id)
            medicine.delete()
            return Response({"delete": True})
        except self.model.DoesNotExist:
            return Response({"delete": False})


class CreateGetOrderView(APIView):
    permission_classes = [IsAuthenticated, ]
    model = Order
    post_serializer_class = MedicinePostSerializer
    get_serializer_class = MedicineGetSerializer
    user_model = User

    def post(self, request):
        data = request.data
        serialized = self.post_serializer_class(data=data)
        if serialized.is_valid():
            serialized.save()
            return Response({"save": True})
        return Response({"save": False})

    def get(self, request):
        id = request.GET.get("id")
        q = request.GET.get("q")
        if q == "single":
            try:
                client = self.user_model.objects.get(id=id)
                queryset = self.model.objects.filter(Q(client=client))
                serialized = self.get_serializer_class(instance=queryset, many=True)
                return Response(serialized.data)
            except self.user_model.DoesNotExist:
                return Response([])
        elif q == "all":
            queryset = self.model.objects.all()
            serialized = self.get_serializer_class(instance=queryset, many=True)
            return Response(serialized.data)
        else:
            return Response([])


class UpdateDeleteOrderView(APIView):
    model = Order
    def post(self, request):
        data = request.data
        try:
            order = self.model.get(id=data['id'])
            order.total_price = data['total_price']
            order.description = data['description']
            order.save()
            return Response({"success": True})
        except self.model.DoesNotExist:
            return Response({"success": False})

    def get(self, request):
        try:
            id = request.GET.get("id")
            order = self.model.objects.get(id=id)
            order.delete()
            return Response({"delete": True})
        except self.model.DoesNotExist:
            return Response({"delete": False})


class CreateGetOrderMedicineView(APIView):
    permission_classes = [IsAuthenticated, ]
    model = OrderMedicine
    post_serializer_class = OrderMedicinePostSerializer
    get_serializer_class = OrderMedicineGetSerializer
    medicine_model = Medicine

    def post(self, request):
        data = request.data
        serialized = self.post_serializer_class(data=data)
        if serialized.is_valid():
            serialized.save()
            return Response({"save": True})
        return Response({"save": False})

    def get(self, request):
        id = request.GET.get("id")
        try:
            medicine = self.medicine_model.objects.get(id=id)
            queryset = self.model.objects.filter(Q(medicine=medicine))
            serialized = self.get_serializer_class(instance=queryset, many=True)
            return Response(serialized.data)
        except self.medicine_model.DoesNotExist:
            return Response([])


class UpdateDeleteOrderMedicineView(APIView):
    model = OrderMedicine
    def post(self, request):
        data = request.data
        try:
            orderMedicine = self.model.get(id=data['id'])
            orderMedicine.dosage = data['dosage']
            orderMedicine.save()
            return Response({"success": True})
        except self.model.DoesNotExist:
            return Response({"success": False})

    def get(self, request):
        try:
            id = request.GET.get("id")
            orderMedicine = self.model.objects.get(id=id)
            orderMedicine.delete()
            return Response({"delete": True})
        except self.model.DoesNotExist:
            return Response({"delete": False})
