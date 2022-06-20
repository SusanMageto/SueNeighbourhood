from django.urls import path

from .views import *

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', log_in, name='login'),
    path('logout/', log_out, name='logout'),
    path('admindash/', admin_dashboard, name='admin_dashboard'),
    path('profile/<username>/', profile, name='profile'),
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('delete/profile/<int:id>/', delete_profile, name='delete_profile'),
]