from django.db import models
from django.utils import timezone


class todo(models.Model):
    topic = models.CharField(max_length=50)
    venue = models.CharField(max_length=250)
    slot = models.DateTimeField(default=timezone.now)




class myform(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()


# Create your models here.
