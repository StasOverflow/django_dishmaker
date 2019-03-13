from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json


class PageUpdateConsumer(WebsocketConsumer):

    def connect(self):
        print(self.scope)
        # self. = self.scope['url_route']['kwargs']['room_name']
        self.group_name = self.channel_name + '_group'

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )
