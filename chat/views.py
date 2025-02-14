from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import json
from datetime import datetime
from .models import Message

# Create your views here.
class MessageView(View):
    def get(self, request, room_name):
        last_message_id = int(request.GET.get('last_message_id', 0))
        messages = Message.objects.filter(
            room_name=room_name,
            pk__gt=last_message_id
        ).order_by('-pk')[:10]
        
        response_data = []
        for msg in messages:
            response_data.append({
                'id': msg.pk,
                'sender': msg.sender,
                'text': msg.text,
                'datetime': msg.datetime.isoformat()
            })
            
        return JsonResponse(response_data, safe=False)

class SendMessageView(View):
    def post(self, request, room_name):
        data = json.loads(request.body)
        message = Message.objects.create(
            room_name=room_name,
            sender=request.user.username,
            text=data['message']
        )
        return JsonResponse({'status': 'success'})
