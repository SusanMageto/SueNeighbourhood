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
def home(request):
    # projects = Project.objects.all()
    # proje = Project.objects.all().order_by('-id')[0]

    # context={
    #     'proje':proje,
    #     'projects':projects,
    # }
    return render(request, 'home.html')   


