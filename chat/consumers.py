import json
from channels.generic.websocket import AsyncWebsocketConsumer
from users.models import Profile
from django.contrib.auth.models import User
from asgiref.sync import async_to_sync

class ChatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

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
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chatroom_message',
                'message': message,
                'username': username,
            }
        )

    async def chatroom_message(self, event):
        message = event['message']
        username = event['username']
        userobj=User.objects.filter(username=username)[0]
        st=Profile.objects.filter(user=userobj)[0]
        if len(st.messages)+len(message)>10000:
            st.messages=st.messages[len(st.messages)+len(message)-10000:]+" "+message
        else:
            st.messages=st.messages+message
        st.save()
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
        }))

    pass
