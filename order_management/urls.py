from django.urls import path
from .views import *
app_name = 'order_management'

urlpatterns = [
    path('insert-get-desease', CreateGetDeseaseView.as_view()),
    path('delete-update-desease', UpdateDeleteDeseaseView.as_view()),
    path('insert-get-medicine', CreateGetMedicineView.as_view()),
    path('delete-update-medicine', UpdateDeleteMedicineView.as_view()),
    path('insert-get-order', CreateGetOrderView.as_view()),
    path('get-order-history', OrderHistoryView.as_view()),
    path('delete-update-order', UpdateDeleteOrderView.as_view()),
    path('get-order-products', OrderProductsView.as_view()),
    path('update-order-status', UpdateOrderStatusView.as_view()),
]