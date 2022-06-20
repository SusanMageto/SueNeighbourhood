from django.db import models

# Create your models here.

class Neighbourhood(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Buseiness(models.Model):
    name = models.CharField(max_length=300)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Contacts(models.Model):
    department = models.CharField(max_length=300)
    contacts = models.CharField(max_length=300)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)

    def __str__(self):
        return self.department

class Post(models.Model):
    name = models.CharField(max_length=300)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.FileField(upload_to='post_image', null=True, blank=True)

    def __str__(self):
        return self.name

