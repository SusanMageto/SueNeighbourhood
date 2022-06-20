from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout 
from  .forms import SignUpForm, LoginForm, EditProfileForm
from django.urls import reverse
from .models import User, Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            messages.success(request, "Congratulations, you are now a registered user!")
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def log_in(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            # We check if the data is correct
            user = authenticate(email=email, password=password)
            if user:  # If the returned object is not None
                login(request, user)  # we connect the user
                return redirect('home')
            else:  # otherwise an error will be displayed
                messages.error(request, 'Invalid email or password')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})



def log_out(request):
    logout(request)
    return redirect(reverse('home'))    



@login_required
def profile(request, username):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    return render(request, 'profile.html', {'profile': profile, 'user': user}) 


@login_required
def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            prof = form.save(commit=False)

            user = User.objects.get(id=request.user.id)
            profile = Profile.objects.get(user=user)
            user.username = username
            prof.user=user
            # profile.about_me = about_me
            # profile.location = location
            # profile.neighbourhood = neighbourhood
            # if image:
            #     profile.image = image
            prof.save()
            return redirect("home")
    else:
        form = EditProfileForm(request.user.username)
    return render(request, "edit_profile.html", {'form': form})   

@login_required
def delete_profile(request, id):
    profile = get_object_or_404(Profile, id = id)
    profile.delete()
    messages.success(request,"profile was deleted successfully")
    return redirect('home')       
# @login_required
# def edit_profile(request):
#     if request.method == "POST":
#         form = EditProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             about_me = form.cleaned_data["about_me"]
#             username = form.cleaned_data["username"]
#             image = form.cleaned_data["image"]

#             user = User.objects.get(id=request.user.id)
#             profile = Profile.objects.get(user=user)
#             user.username = username
#             user.save()
#             profile.about_me = about_me
#             profile.location = location
#             profile.neighbourhood = neighbourhood
#             if image:
#                 profile.image = image
#             profile.save()
#             return redirect("profile", username=user.username)
#     else:
#         form = EditProfileForm(request.user.username)
#     return render(request, "edit_profile.html", {'form': form})       

def admin_dashboard(request):
    if request.user.is_authenticated and request.user.is_staff:
        profiles = Profile.objects.all().order_by('-id')
        context = {
            'profiles':profiles,
        }

        return render(request, 'admin.html', context)