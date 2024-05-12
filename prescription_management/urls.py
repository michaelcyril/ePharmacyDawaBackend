from django.urls import path
from .views import *
app_name = 'prescription_management'

urlpatterns = [
    path('insert-get-prescription', PrescriptionView.as_view()),
    path('delete-update-prescription', DeleteUpdatePrescription.as_view()),
    path('change-prescription-status', ChangePrescriptionStatusView.as_view()),
]
