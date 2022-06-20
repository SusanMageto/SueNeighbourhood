from django.shortcuts import render, redirect
from .models import *
from users.models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

@login_required
def home(request):
    profile = Profile.objects.get(user=request.user)
    posts = Post.objects.filter(neighbourhood=profile.neighbourhood_name).order_by('-id')

    context={
        'posts':posts,
    }
    return render(request, 'home.html',context)   


def postnews(request):
    if request.user.is_authenticated:
        form = PostForm() 
        profile = Profile.objects.get(user=request.user)
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES)
           
            
            if form.is_valid():  
                project = form.save(commit=False)   
                project.user = request.user
                project.neighbourhood = profile.neighbourhood_name
                project.save()
                messages.success(request,"post was added successfully")
                return redirect('home')
    
        context = {
            'form':form,
        }
        return render(request, 'postprojectpage.html', context)