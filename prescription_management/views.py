from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from user_management.models import User


class PrescriptionView(APIView):
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
        try:
            q = request.GET.get("q")
            if q == "s":
                id = request.GET.get("id")
                user = User.objects.get(id=id)
                prescription = Prescription.objects.filter(user=user)
                serialized = PrescriptionGetSerializer(instance=prescription, many=True)
                return Response(serialized.data)
            elif q == "a":
                prescription = Prescription.objects.all()
                serialized = PrescriptionGetSerializer(instance=prescription, many=True)
                return Response(serialized.data)
            else:
                return Response([])

        except User.DoesNotExist:
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
