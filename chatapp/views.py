from django.shortcuts import get_object_or_404, render,redirect
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *

def index(request):
    return render(request, "chatapp/index.html")


@login_required
def room(request, room_name):


    college=get_object_or_404(College,id=room_name)
    form=ChatmessageCreateForm()
    chat_group=get_object_or_404(ChatGroup,college=college)
    chat_messages=chat_group.messages.all()[:30]
    if request.htmx:
        print('here')
        form=ChatmessageCreateForm(request.POST)
        print(request.POST)
        if form.is_valid():
            message=form.save(commit=False)
            message.group=chat_group
            print(message.group)
            message.author=request.user
            print(message.author)
            message.save()
            context={
                'message':message,
                'user':request.user
            }
            return render(request,'partials/chat_message_p.html',context)
    context={'chat_messages':chat_messages,'form':form,'id':room_name}
    return render(request, "chatapp/room.html", context)

