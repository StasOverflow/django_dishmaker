from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import json


class TestConsumer(WebsocketConsumer):
    def connect(self):
        async_to_sync(self.channel_layer.group_add)("tests", self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)("tests", self.channel_name)

    def receive(self, text_data=None, bytes_data=None):
        pass

    def tests_message(self, event):
        self.send(text_data=event['text'])


def ws_reload_page():
    layer = get_channel_layer()
    async_to_sync(layer.group_send)(
        "tests",
        {
            "type": "tests.message",
            "text": json.dumps({'message': 'reloading'}),
        }
    )
