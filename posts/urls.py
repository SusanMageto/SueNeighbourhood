from django.urls import path

from .views import *



urlpatterns = [
    path('', home, name='home'),
    path('postnews/', postnews, name='postnews'),
    path('create-bsn/', create_bsn, name='postbsn'),
    path('create-hood/', create_neighbourhood, name='posthood'),
    path('postdept/', postdept, name='postdept'),
    path('post/<int:id>/', post_details, name='post_details'),
    path('delete/bsn/<int:id>/', delete_business, name='delete_business'),
    path('update/bsn/<int:id>/', edit_business, name='edit_business'),
    path('business/<int:id>/', find_business, name='find_business'),
    path('hood/<int:id>/', find_neigbourhood, name='find_neigbourhood'),
    path('delete/hood/<int:id>/', delete_neigbourhood, name='delete_neigbourhood'),
    path('update/hood/<int:id>/', edit_neigbourhood, name='edit_neigbourhood'),
    path('search/', search, name='search'),
    
]