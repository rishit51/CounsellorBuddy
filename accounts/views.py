from django.shortcuts import render,redirect
from .forms import *
from .models import User,StudentProfile
from django.contrib.auth.decorators import login_required
from django.contrib.messages import success
# Create your views here.

def counsellor(request):
    return render(request,'accounts/counsellor-create.html')
@login_required(login_url='account_login')
def create_profile(request):
    if request.user.role==User.Role.STUDENT:
        profile=StudentProfile.objects.get(user=request.user)
        form=StudentProfileForm(instance=profile)
        context={'form':form}        
        if request.method=="POST":
            form=StudentProfileForm(data=request.POST,files=request.FILES,instance=profile)
            if form.is_valid():
                form.save()
                success(request,"Your Profile has been Created Successfully")
                return redirect('home')
        return render(request,'accounts/student-create.html' ,context)
    
    profile=CounsellorProfile.objects.get(user=request.user)
    form=CounsellorProfileForm(instance=profile)
    if request.method=="POST":
            form=CounsellorProfileForm(data=request.POST,files=request.FILES,instance=profile)
            if form.is_valid():
                form.save()
                success(request,"Your Profile has been Created Successfully")
                return redirect('home')
    return render(request,'accounts/counsellor-create.html',{'form':form})

@login_required(login_url='account_login')
def profile_view(request):
    context={}
    if request.user.role==User.Role.STUDENT:
         userprofile=StudentProfile.objects.get(user=request.user)
         context={'userprofile':userprofile}

         return render(request,'accounts/student_profile_view.html',context)
    if request.user.role==User.Role.COUNSELLOR:
         userprofile=CounsellorProfile.objects.get(user=request.user)
         context={'counsellor':userprofile}

         return render(request,'accounts/counsellor_profile.html',context)