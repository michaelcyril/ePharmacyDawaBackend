from django.urls import path
from .views import *
app_name = 'user_management'

urlpatterns = [
    path('register-pharmacist', RegisterUser.as_view()),
    path('verify-phone', VerifyPhone.as_view()),
    path('verify-otp', VerifyOtp.as_view()),
    path('complete-profile', CompleteUserProfile.as_view()),
    path('all-users', AllUser.as_view()),
]
