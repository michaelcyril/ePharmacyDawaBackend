from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from .models import *
from .serializer import *
from django.contrib.auth import authenticate, login, update_session_auth_hash

from BeemAfrica import Authorize, AirTime, OTP, SMS
import math, random

# Create your views here.

def pushMessage(otp, phone):
    Authorize('478040a68e5f755d',
              'ZTVkMzUwYWI5NjMwYjM2Zjc0ZTY1ZGQ5ZmQzZWNjNTMwYzRkOTEyYWRlODdhNWIxYmExYmQxOGZkMGNiODdiYg==')
    request = SMS.send_sms(
        'OTP for grocery app ' + otp,
        phone,
        sender_id='MC-Official'
    )
    return request


def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP


class VerifyPhone(APIView):
    @staticmethod
    def post(request):
        try:
            data = request.data
            users = User.objects.filter(phone=data['phone'])
            otp_code = generateOTP()
            print(otp_code)
            if len(users) == 0:
                user_data = {
                    "username": data['phone'],
                    "otp": otp_code,
                    "phone": data['phone'],
                    "role": data["role"],
                    "password": "123"
                }
                serializer = UserSerializer(data=user_data)
                if serializer.is_valid():
                    user = serializer.save()
                    pushMessage(otp_code, data['phone'])
                    message = {'request': True}
                    return Response(message)
                return Response({'request': False, 'errors': serializer.errors})
            user = User.objects.get(phone=data['phone'])
            # if user.role == data['role']:
            user.otp = otp_code
            user.otp_created_at = timezone.now()
            # pushMessage(otp_code, data['phone'])
            user.save()
            return Response({"request": True})
            # return Response({'request': False})
        except Exception as e:
            print(e)
            return Response({'request': False})


# {
# "phone":"0693331836",
# "type":"NORMAL"
# }


class VerifyOtp(APIView):
    @staticmethod
    def post(request):
        try:
            data = request.data
            print(data)
            users = User.objects.filter(phone=data['phone'])
            if len(users) == 0:
                return Response({'success': False})
            user1 = User.objects.get(phone=data['phone'])
            if user1.otp == data['otp']:
                current_time = timezone.now()
                time_difference = current_time - user1.otp_created_at
                print(user1.otp_created_at)

                if not time_difference.total_seconds() <= 240:
                    return Response({"success": False, "message": "OTP expired"})
                user = authenticate(username=data['phone'], password="123")
                if user is not None:
                    login(request, user)
                    token, created = Token.objects.get_or_create(user=user)
                    user_id = User.objects.get(username=data['phone'])
                    user_info = UserSerializer(instance=user_id, many=False).data
                    print(user_info)
                    response = {
                        'token': token.key,
                        'user': user_info,
                        "success": True
                    }

                    return Response(response)
                else:
                    response = {
                        'msg': 'Invalid username or password', "success": False
                    }

                    return Response(response)
            return Response({"success": False})
        except:
            return Response({"success": False})


# {
# "phone":"0693331836",
# "otp":"6254"
# }


class CompleteUserProfile(APIView):
    @staticmethod
    def post(request):
        try:
            data = request.data
            try:
                user = User.objects.get(id=data['id'])
                user.age = data['age']
                user.gender = data['gender']
                user.address = data['address']
                user.first_name = data['name']
                user.profileComplete = True
                user.save()
                return Response({"update": True})
            except USer.DoesNotExist:
                return Response({"update": False, "message": "User Does Not Exist"})
        except:
            return Response({"update": False, "message": "Error Occured"})

# {
#     "id":"",
#     "age": "12",
#     "gender": "MALE",
#     "address": 12
# }


class AllUser(APIView):
    @staticmethod
    def get(request):
        users = User.objects.values("id").all()
        return Response(users)


class RegisterUser(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            phone = data['phone']
            user = User.objects.filter(phone=phone)
            if user:
                message = {'save': False, 'message': 'phone number already exists'}
                return Response(message, status=status.HTTP_400_BAD_REQUEST)
            if data['role'] == "ADMIN":
                userr = serializer.save()
                return Response({"save": True})
            else:
                return Response({"save": False, "message": "Only For Pharmacist"})

        message = {'save': False, 'errors': serializer.errors}
        return Response(message)

    @staticmethod
    def get(request):
        users  = User.objects.all()
        return Response(UserSerializer(instance=users, many=True).data)

# {
#     "username":"255693331837",
#     "password":"123",
#     "phone":"255693331837",
#     "role":"ADMIN",
#     "age": 45,
#     "gender": "MALE",
#     "address": "Kimara",
#     "profileComplete": True
# }
