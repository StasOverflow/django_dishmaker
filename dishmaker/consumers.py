from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json


class PageUpdateConsumer(WebsocketConsumer):

    def connect(self):
        async_to_sync(self.channel_layer.group_add)(
            'main_page_viewers',
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            'main_page_viewers',
            self.channel_name
        )

    def receive(self, text_data=None, blah_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        print('iv\'e got da message')

        async_to_sync(self.channel_layer.group_send)(
            'main_page_viewers',
            {
                'type': 'chat_message',
                'message': message
            }
        )

    def chat_message(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            'message': message
        }))
