from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from .serializer import *
from .models import *
from user_management.models import User
from django.db.models import Q


class CreateGetDeseaseView(APIView):
    # permission_classes = [IsAuthenticated, ]
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
            return Response({"update": True})
        except self.model.DoesNotExist:
            return Response({"update": False})

    def get(self, request):
        try:
            id = request.GET.get("id")
            desease = self.model.get(id=id)
            desease.delete()
            return Response({"delete": True})
        except self.model.DoesNotExist:
            return Response({"delete": False})


class CreateGetMedicineView(APIView):
    permission_classes = [AllowAny, ]
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
        query_type = request.GET.get("query_type")
        if query_type == "disease":
            disease_id = request.GET.get("disease_id")
            try:
                desease = Desease.objects.get(id=disease_id)
                queryset = self.model.objects.filter(desease=desease, active=True)
                serialized = self.get_serializer_class(instance=queryset, many=True)
                print(serialized.data)
                return Response(serialized.data)
            except Desease.DoesNotExist:
                return Response([])
        if query_type == "all_disease":
            queryset = self.model.objects.filter(type="DESEASE", active=True)
            serialized = self.get_serializer_class(instance=queryset, many=True)
            return Response(serialized.data)
        elif query_type == "otc":
            queryset = self.model.objects.filter(type="OTC", active=True)
            serialized = self.get_serializer_class(instance=queryset, many=True)
            return Response(serialized.data)
        elif query_type == "all":
            queryset = self.model.objects.filter(active=True)
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
            medicine.description = data['description']
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
            medicine.active = False
            medicine.save()
            return Response({"delete": True})
        except self.model.DoesNotExist:
            return Response({"delete": False})


class CreateGetOrderView(APIView):
    permission_classes = [AllowAny, ]
    model = Order
    post_serializer_class = OrderPostSerializer
    get_serializer_class = OrderGetSerializer
    user_model = User

    def post(self, request):
        data = request.data
        serialized = self.post_serializer_class(data=data)
        if serialized.is_valid():
            order_id = f"ORDER{timezone.now().strftime('%H%M%S')}"
            serialized.save(order_id=order_id)
            return Response({"save": True})
        return Response({"save": False})

    def get(self, request):
        query_type = request.GET.get("query_type")
        if query_type == "client_order":
            try:
                client_id = request.GET.get("client_id")
                order_status = request.GET.get("order_status")
                client = self.user_model.objects.get(id=client_id)
                if order_status:
                    queryset = self.model.objects.filter(client=client, status=order_status, active=True)
                    serialized = self.get_serializer_class(instance=queryset, many=True)
                    return Response(serialized.data)
                else:
                    queryset = self.model.objects.filter(client=client, active=True)
                    serialized = self.get_serializer_class(instance=queryset, many=True)
                    return Response(serialized.data)
            except self.user_model.DoesNotExist:
                return Response([])
        elif query_type == "pharmacist_order":
            order_status = request.GET.get("order_status")
            if order_status:
                queryset = self.model.objects.filter(status=order_status, active=True)
                serialized = self.get_serializer_class(instance=queryset, many=True)
                return Response(serialized.data)
            else:
                queryset = self.model.objects.filter(active=True)
                serialized = self.get_serializer_class(instance=queryset, many=True)
                return Response(serialized.data)
        else:
            return Response([])


class OrderHistoryView(APIView):
    permission_classes = [AllowAny, ]
    model = Order
    get_serializer_class = OrderGetSerializer

    def get(self, request):
        queryset = self.model.objects.filter(status="PENDING")
        serialized = self.get_serializer_class(instance=queryset, many=True)
        return Response(serialized.data)


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
            order.active = False
            order.save()
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


class OrderProductsView(APIView):
    permission_classes = [AllowAny, ]
    model = OrderMedicine
    get_serializer_class = OrderMedicineGetSerializer

    def get(self, request):
        order_id = request.GET.get("order_id")
        try:
            order = Order.objects.get(id=order_id)
            queryset = self.model.objects.filter(order=order)
            serialized = self.get_serializer_class(instance=queryset, many=True)
            return Response(serialized.data)
        except Order.DoesNotExist:
            return Response([])


class UpdateOrderStatusView(APIView):
    model = Order
    def post(self, request):
        data = request.data
        try:
            order = self.model.objects.get(id=data['id'])
            order.status = data['status']
            order.save()
            return Response({"success": True})
        except self.model.DoesNotExist:
            return Response({"success": False})