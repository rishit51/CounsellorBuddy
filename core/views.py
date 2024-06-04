from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponseRedirect
# Create your views here.
from .forms import ReviewForm
def home(request):
    top_colleges=College.objects.all()[:5]
    context={'colleges':top_colleges}


    return render(request,'core/index.html',context)

def profile(request):


    return render(request,'core/counsellor.html')

def college(request,id):
    try:
        college = College.objects.get(pk=id)
        form=ReviewForm()
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.user = request.user
                review.college = college
                review.save()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            
        context={'college':college,'form':form}

    except:
        return render(request,'404.html')    
    return render(request,'core/college.html',context)


def colleges(request):
    colleges=College.objects.all()
    context={'colleges':colleges}
    return render(request,'core/colleges.html',context)