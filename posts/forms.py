from .models import *
from django.forms import ModelForm


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['name', 'content', 'image']

class BuseinessForm(ModelForm):
    class Meta:
        model = Buseiness
        fields = ['name','email']

class ContactsForm(ModelForm):

    class Meta:
        model = Contacts
        fields = ['department', 'contacts']        

