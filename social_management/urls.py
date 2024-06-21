from django.urls import path
from .views import *
app_name = 'social_management'

urlpatterns = [
    path('conversation-view', ConversationView.as_view()),
    path('message-view', MessageView.as_view()),
    path('conversation-to-seen-view', SeenView.as_view()),
]