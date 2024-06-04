from .models import *
from django import forms
from django.forms import ModelForm




class ChatmessageCreateForm(ModelForm):
    class Meta:
        model=GroupMessage
        fields=['body']
        widgets={
            'body':forms.TextInput(attrs={'autofocus':True,'placeholder':'Add message...','class':'p-2 text-black w-full rounded-md' ,'maxlength':'300'})
        }