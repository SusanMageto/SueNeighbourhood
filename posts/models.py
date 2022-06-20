from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.

class Neighbourhood(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Buseiness(models.Model):
    name = models.CharField(max_length=300)
    neighbourhood = models.CharField(max_length=300)
    def __str__(self):
        return self.name


class Contacts(models.Model):
    department = models.CharField(max_length=300)
    contacts = models.CharField(max_length=300)
    neighbourhood = models.CharField(max_length=300)

    def __str__(self):
        return self.department

class Post(models.Model):
    name = models.CharField(max_length=300)
    neighbourhood = models.CharField(max_length=300)
    content = models.TextField()
    image = models.FileField(upload_to='post_image', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

