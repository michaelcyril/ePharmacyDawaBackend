from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from user_management.models import User


class PrescriptionView(APIView):
    model = Prescription
    get_serializer_class = PrescriptionGetSerializer
    post_serializer_class = PrescriptionPostSerializer
    user_model = User
    @staticmethod
    def post(request):
        data = request.data
        try:
            serialized = PrescriptionPostSerializer(data=data)
            isvalid = serialized.is_valid()
            if isvalid:
                serialized.save()
                return Response({"save": True})
            return Response({"save": False, "errors": serialized.errors})
        except:
            return Response({"save": False, "errors": "Error Occured"})

    @staticmethod
    def get(request):
        query_type = request.GET.get("query_type")
        if query_type == "client_prescription":
            try:
                client_id = request.GET.get("client_id")
                prescription_status = request.GET.get("prescription_status")
                user = self.user_model.objects.get(id=client_id)
                if prescription_status:
                    queryset = self.model.objects.filter(user=user, status=prescription_status, active=True)
                    serialized = self.get_serializer_class(instance=queryset, many=True)
                    return Response(serialized.data)
                else:
                    queryset = self.model.objects.filter(client=client, active=True)
                    serialized = self.get_serializer_class(instance=queryset, many=True)
                    return Response(serialized.data)
            except self.user_model.DoesNotExist:
                return Response([])
        elif query_type == "pharmacist_prescription":
            prescription_status = request.GET.get("prescription_status")
            if order_status:
                queryset = self.model.objects.filter(status=prescription_status, active=True)
                serialized = self.get_serializer_class(instance=queryset, many=True)
                return Response(serialized.data)
            else:
                queryset = self.model.objects.filter(active=True)
                serialized = self.get_serializer_class(instance=queryset, many=True)
                return Response(serialized.data)
        else:
            return Response([])


class DeleteUpdatePrescription(APIView):
    @staticmethod
    def post(request):
        try:
            data = request.data
            prescription = Prescription.objects.get(id=data['id'])
            # prescription.litre = data['litre']
            prescription.save()
            return Response({"update": True})
        except:
            return Response({"update": False, "error": "Water Does Not Exists"})


    @staticmethod
    def get(request):
        try:
            id = request.GET.get("id")
            prescription = Prescription.objects.get(id=id)
            prescription.delete()
            return Response({"delete": True})
        except Prescription.DoesNotExist:
            return Response({"delete": False, "error": "Water Does Not Exists"})


class ChangePrescriptionStatusView(APIView):
    # permission_classes = [IsAuthenticated, ]
    model = Prescription
    def post(self, request):
        data = request.data
        try:
            prescription = self.model.objects.get(id=data['id'])
            prescription.status = data['status_to']
            prescription.save()
            return Response({"chenge": True})
        except self.model.DoesNotExist:
            return Response({"change": False})

# {
#     "id": "nnnnnn",
#     "status_to": ""
# }
