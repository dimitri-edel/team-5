from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from .models import Message, Connection

@receiver(post_save, sender=Message)
def broadcast_message(sender, instance, **kwargs):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f"chat_{instance.room_name}",
        {'type': 'message',
         'sender': instance.sender,
         'text': instance.text}
    )

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"
        
        # Store connection in database
        Connection.objects.create(
            channel=self.channel_name,
            room=self.room_name
        )
        
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        
        self.accept()

    def disconnect(self, close_code):
        Connection.objects.filter(channel=self.channel_name).delete()
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )