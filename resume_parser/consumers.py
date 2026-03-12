# consumers.py in your Django app
from channels.generic.websocket import AsyncWebsocketConsumer
import json

import logging

# Configure logging
logger = logging.getLogger(__name__)

class NotificationConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Log when a consumer instance is created
        logger.info("MyConsumer instance created")

    async def connect(self):
        self.user_id = self.scope['url_route']['kwargs']['user_id']  # Assuming you capture user_id from the URL
        self.user_group_name = f'user_notifications_{self.user_id}'

        # Log the connection
        logger.info(f'WebSocket connection to room {self.user_group_name}')
        # Join user-specific group
        await self.channel_layer.group_add(
            self.user_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave user-specific group
        await self.channel_layer.group_discard(
            self.user_group_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        pass

    # This handler is called when sending messages to the group
    async def user_notification(self, event):
        message = event['message']
        req_no = event['req_no']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'req_no': req_no
        }))
