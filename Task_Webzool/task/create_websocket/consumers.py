import json
from channels.generic.websocket import AsyncWebsocketConsumer
from main.models import Comments
from main.serializers import CommentSerializer

class CommentConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['pk']
        self.room_group_name = f"product_{self.room_name}_comments"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data_json = json.loads(text_data)
        serializer = CommentSerializer(data=data_json)

        if serializer.is_valid():
            comment = serializer.save()
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'comment_message',
                    'comment': serializer.data
                }
            )

    async def comment_message(self, event):
        await self.send(text_data=json.dumps(event['comment']))
