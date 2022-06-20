from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('postnews/', postnews, name='postnews'),
    path('postbsn/', postbsn, name='postbsn'),
    path('post/<int:id>/', post_details, name='post_details'),
    
]