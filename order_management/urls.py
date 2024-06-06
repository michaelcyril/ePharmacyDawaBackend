from django.urls import path
from .views import *
app_name = 'order_management'

urlpatterns = [
    path('insert-get-desease', CreateGetDeseaseView.as_view()),
    path('delete-update-desease', UpdateDeleteDeseaseView.as_view()),
    # path('change-desease-status', ChangePrescriptionStatusView.as_view()),
]