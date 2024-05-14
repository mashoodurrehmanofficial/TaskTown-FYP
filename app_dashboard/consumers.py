# chat/consumers.py

import json
from asgiref.sync import sync_to_async

from channels.generic.websocket import AsyncWebsocketConsumer




class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        from .utils import fetch_messages 
        self.project_id = self.scope['url_route']['kwargs']['project_id']  # Extract project ID from URL
        self.room_name = f'project_{self.project_id}_room'
        self.room_group_name = f'chat_{self.room_name}'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # Fetch and send existing messages to the client
        messages = await sync_to_async(fetch_messages)(self.project_id)
        # await self.send(text_data=json.dumps(messages))
        await self.accept()
        for message in messages: 
            await self.send(text_data=json.dumps({
                'message': message
            }))


    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        from .utils import save_message
        
        from app.models import MessagesTable,ProfilesTable
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user_id = self.scope['user'].id  # Assuming the user is authenticated
         
        
            # Call the synchronous function asynchronously
        await sync_to_async(save_message)(user_id, message, self.project_id)

        # Save message to the database
        # MessagesTable.objects.create(user=profile, content=message, project_id=self.project_id)
        # await sync_to_async(MessagesTable.objects.create)(user=profile, content=message, project_id=self.project_id)


        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': {"text":message,'user_id':user_id},
                'user_id':user_id
            }
        )

    async def chat_message(self, event):
        message = event['message']
        user_id = event['user_id']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'user_id':user_id
        }))
