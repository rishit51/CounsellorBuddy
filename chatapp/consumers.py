# chat/consumers.py
import json
from core.models import *
from .models import *
from django.shortcuts import get_object_or_404
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.template.loader import render_to_string
 
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.user=self.scope['user']
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.college = get_object_or_404(College,id=self.room_name)
        self.chat_room=get_object_or_404(ChatGroup,college=self.college)
        
        if self.user not in self.chat_room.users_online.all():
            self.chat_room.users_online.add(self.user)
            self.update_count()
    
      
        async_to_sync(self.channel_layer.group_add)(
            str(self.chat_room.id),self.channel_name
        )
        self.accept()

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            str(self.chat_room.id),self.channel_name
        )
        if self.user in self.chat_room.users_online.all():
            self.chat_room.users_online.remove(self.user)
            self.update_count()

    # Receive message from WebSocket

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["body"]
   
        message=GroupMessage.objects.create(body=message,author=self.user,group=self.chat_room)
        
        event={'type':'message_handler','message_id':message.id}
        async_to_sync(self.channel_layer.group_send)(
            str(self.chat_room.id),event
        )

    def message_handler(self, event):
        message_id=event['message_id']
        message=GroupMessage.objects.get(id=message_id) 
        context={'message':message,'user':self.user}
        html=render_to_string('partials/chat_message_p.html',context)
        self.send(text_data=html)
    
    def update_count(self):
        online_count=self.chat_room.users_online.count()
        event={'type':'online_count_handler','online_count':online_count}
        async_to_sync(self.channel_layer.group_send)(str(self.chat_room.id),event)
    
    def online_count_handler(self,event):
        online_count=event['online_count']
        context={'online_count':online_count}
        html=render_to_string('partials/online_count_p.html',context)
        self.send(text_data=html)