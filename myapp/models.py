from django.db import models
from django.contrib.auth.models import User

class projectUser(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


class slide(models.Model):
    slide_text = models.CharField(max_length=500, blank=True, null=True)
    file_type = models.CharField(max_length=10, blank=True, null=True)
    slide = models.FileField(blank=True, null=True)
    

class project(models.Model):
    user = models.ForeignKey(projectUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    slides = models.ManyToManyField(slide, blank=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.user)














