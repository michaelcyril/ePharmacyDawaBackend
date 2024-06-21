from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator
from social_management.consumers import ChatRoomConsumer

application = ProtocolTypeRouter({
    #Empty
    #"http": get_asgi_application(),
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
                URLRouter(
                [
                    re_path(r"^chat-room-conversation/(?P<chat_id>)", ChatRoomConsumer.as_asgi()),
                ]
            )
        )
    )
})