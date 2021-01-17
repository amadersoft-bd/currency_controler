from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import DateTimeField
import datetime
from django.utils import timezone
# Create your models here.

class Notification(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    duration = models.DateField(null=True)
    title= models.CharField(max_length=200,null=True,blank=True)
    body = models.TextField(max_length=300,null=True,blank=True)
    status = models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.title
