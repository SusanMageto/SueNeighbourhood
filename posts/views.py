from django.shortcuts import render, redirect
from .models import *
from users.models import *
from users.forms import *
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
    businesses = Buseiness.objects.filter(neighbourhood=profile.neighbourhood).order_by('-id')
    posts = Post.objects.filter(neighbourhood=profile.neighbourhood).order_by('-id')
    contacts = Contacts.objects.filter(neighbourhood=profile.neighbourhood).order_by('-id')

    context={
        'posts':posts,
        'profile':profile,
        'businesses':businesses,
        'contacts':contacts,
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
                project.neighbourhood = profile.neighbourhood
                project.save()
                messages.success(request,"post was added successfully")
                return redirect('home')
    
        context = {
            'form':form,
        }
        return render(request, 'postprojectpage.html', context)


def post_details(request, id):
    
    post = get_object_or_404(Post, id = id)

    
    context = {
        'post':post,
    }
    
    return render(request, 'details.html', context)        

def create_bsn(request):
    if request.user.is_authenticated:
        form = BuseinessForm() 
        profile = Profile.objects.get(user=request.user)
        if request.method == "POST":
            form = BuseinessForm(request.POST, request.FILES)
           
            
            if form.is_valid():  
                bsn = form.save(commit=False)  
                bsn.neighbourhood = profile.neighbourhood
                bsn.save()
                messages.success(request,"bsn was added successfully")
                return redirect('home')
    
        context = {
            'form':form,
        }
        return render(request, 'postbsnpage.html', context) 



def postdept(request):
    if request.user.is_authenticated:
        form = ContactsForm() 
        profile = Profile.objects.get(user=request.user)
        if request.method == "POST":
            form = ContactsForm(request.POST, request.FILES)
           
            
            if form.is_valid():  
                dept = form.save(commit=False)  
                dept.neighbourhood = profile.neighbourhood
                dept.save()
                messages.success(request,"bsn was added successfully")
                return redirect('home')
    
        context = {
            'form':form,
        }
        return render(request, 'postdeptpage.html', context)   


def search(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        q = request.GET['q']
        if q:
            context = {
                'data' : Buseiness.objects.filter(name__icontains=q and neighbourhood==profile.neighbourhood).order_by('-id'),
            }

            return render(request, 'search.html', context)
        return redirect('home') 

@login_required
def delete_business(request, id):
    bsn = get_object_or_404(Buseiness, id = id)
    bsn.delete()
    messages.success(request,"post was deleted successfully")
    return redirect('home')


def edit_business(request, id):
    bsn = get_object_or_404(Buseiness, id = id)
    

    form = BuseinessForm(request.POST or None, instance=bsn)
    if form.is_valid():
        form.save()
        messages.success(request,"post was updated successfully")
        return redirect('home')
    context = {
        'bsn':bsn,
        'form':form,
    }
    return render(request, 'updatebsn.html', context)     



@login_required
def delete_neigbourhood(request, id):
    hood = get_object_or_404(Neighbourhood, id = id)
    hood.delete()
    messages.success(request,"Neighbourhood was deleted successfully")
    return redirect('home')


def edit_neigbourhood(request, id):
    hood = get_object_or_404(Neighbourhood, id = id)
    

    form = NeighbourhoodForm(request.POST or None, instance=hood)
    if form.is_valid():
        form.save()
        messages.success(request,"Neighbourhood was updated successfully")
        return redirect('home')
    context = {
        'hood':hood,
        'form':form,
    }
    return render(request, 'updatehood.html', context)         

def create_neighbourhood(request):
    if request.user.is_authenticated and request.user.is_staff:
        form = NeighbourhoodForm() 
        if request.method == "POST":
            form = NeighbourhoodForm(request.POST, request.FILES)
           
            
            if form.is_valid():  
                hood = form.save(commit=False)  
                hood.admin = request.user
                hood.save()
                messages.success(request,"Neighbourhood was added successfully")
                return redirect('home')
    
        context = {
            'form':form,
        }
        return render(request, 'posthoodpage.html', context)



def find_neigbourhood(request, id):
    
    hood = get_object_or_404(Neighbourhood, id = id)

    
    context = {
        'hood':hood,
    }
    
    return render(request, 'hooddetails.html', context)  


def find_business(request, id):
    
    bsn = get_object_or_404(Buseiness, id = id)

    
    context = {
        'bsn':bsn,
    }
    
    return render(request, 'bsndetails.html', context)          




