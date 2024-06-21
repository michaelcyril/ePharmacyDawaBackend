import json

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from .models import *
from user_management.models import User
from django.db.models import Q
from .channel_manager import PostToChatChannel


class ConversationView(APIView):
    @staticmethod
    def post(request):
        data = request.data
        user1 = User.objects.get(id=data['initiator'])
        user2 = User.objects.get(id=data['receiver'])
        conversation = Conversation.objects.filter(
            (Q(initiator=user1) & Q(receiver=user2)) | (Q(initiator=user2) & Q(receiver=user1)))
        if len(conversation) >= 1:
            return Response({"save": False, "conv_id": conversation[0].id})
        serialized = ConversationPostSerializer(data=data)
        if serialized.is_valid():
            returned_data = serialized.save()
            return Response({"save": True, "conv_id": returned_data.id})

    @staticmethod
    def get(request):
        try:
            user = User.objects.get(id=request.GET.get('user_id'))
            queryset = Conversation.objects.filter(Q(receiver=user) | Q(initiator=user))
            serialized = ConversationGetSerializer(instance=queryset, many=True)
            return Response(serialized.data)
        except:
            return Response([])


class MessageView(APIView):
    @staticmethod
    def post(request):
        serialized = MessagePostSerializer(data=request.data)
        if serialized.is_valid():
            data = serialized.save()
            conversation = Conversation.objects.get(id=data.conversation_id.id)
            conversation.is_seen = False
            conversation.last_message_user = data.sender.id
            conversation.save()
            toSocket = {
                "id": data.id,
                "sender": data.sender.id,
                'text': data.text,
                'conversation_id': data.conversation_id.id,
                'timestamp': data.timestamp
            }
            toSocket['id'] = str(toSocket['id'])
            toSocket['sender'] = str(toSocket['sender'])
            toSocket['conversation_id'] = str(toSocket['conversation_id'])
            toSocket['timestamp'] = toSocket['timestamp'].isoformat()
            PostToChatChannel(toSocket)
            return Response({"send": True,
                             "message": toSocket['text'],
                             })

        return Response({"send": False})

    @staticmethod
    def get(request):
        conv_id = request.GET.get("conv_id")
        try:
            conv = Conversation.objects.get(id=conv_id)
            queryset = Message.objects.values('id', 'sender', 'text', 'conversation_id', 'timestamp').filter(
                conversation_id=conv).order_by('-timestamp')[:20]
            return Response(queryset)
        except Exception as e:
            print(e)
        except:
            # print("EXCEPTIOMD")
            return Response([])


# {
#     "sender": "hhhhhhhhhhhh",
#     "text": "Hello World ",
#     "conversation_id": "hhhhhhhhhhhh"
# }


class SeenView(APIView):
    @staticmethod
    def post(request):
        data = request.data
        try:
            converssation = Conversation.objects.get(id=data['conversation_id'])
            converssation.is_seen = True
            converssation.save()
            return Response({"updated": True})
        except:
            return Response({"updated": False})

# {
#     "conversation_id": "hhhhhhhhhhhh"
# }

