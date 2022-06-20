from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    email = models.EmailField('email address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username"]


class Neighbourhood(models.Model):
    name = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    occupants = models.IntegerField()
    admin = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
        
class Profile(models.Model):
    about_me = models.TextField()
    image = models.FileField(upload_to='profile_image', null=True, blank=True)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
