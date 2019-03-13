from django.conf.urls import url
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'^ws/order_list/$', consumers.ChatConsumer),
]