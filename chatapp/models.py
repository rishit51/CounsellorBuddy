from django.db import models
import uuid
from accounts.models import User,StudentProfile
from accounts.models import CounsellorProfile
from core.models import College
# Create your models here.
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


class ChatGroup(models.Model):
    college=models.OneToOneField(College,related_name='chat_room',on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.college.name}'
    users_online=models.ManyToManyField(User,related_name='online_in_groups',blank=True)


class GroupMessage(models.Model):
    group=models.ForeignKey(ChatGroup,on_delete=models.CASCADE,related_name='messages')
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='group_messages')
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.username}:{self.body}'
    class Meta:
        ordering=['-created']
    def is_counsellor(self):
        return self.author.role=='COUNSELLOR'   