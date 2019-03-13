# chat/routing.py
from django.urls import path

from dishmaker import consumers

websocket_urlpatterns = [
    path('ws/', consumers.PageUpdateConsumer),
]
