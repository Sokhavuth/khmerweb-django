#home/models.py
from django.db import models
from django.conf import settings

# Create your models here.
class Media(models.Model):
    id = models.CharField(primary_key=True,max_length=500)
    title = models.CharField(max_length=500)
    content = models.TextField(max_length=500)
    thumb = models.CharField(max_length=500)
    video = models.CharField(max_length=500)
    category = models.CharField(max_length=500)
    date = models.DateTimeField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)