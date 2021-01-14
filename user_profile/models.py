import agent.models
from .utils import create_new_ref_number
from django.db import models
from django.contrib.auth.models import User
class Package(models.Model):
    package_name = models.CharField(max_length=200,default='primary')
    package_amount = models.FloatField(default=0)
    duration = models.TimeField(default=0)
    description = models.TextField(max_length=300,null=True,blank=True)
    def __str__(self):
        return self.package_name
        
class UsePositionStatus(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    status_id = models.CharField(max_length=250,unique=True)
    def __str__(self):
        return self.name
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True, blank=True)
    #user_id = models.CharField(max_length=250,unique=True)
    full_name= models.CharField(max_length=200,null=True,blank=True)
    address = models.TextField(max_length=300,null=True,blank=True)
    country = models.CharField(max_length=200,null=True,blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d',null=True,blank=True)
    #password 
    mobile_no = models.CharField(max_length=20,null=True,blank=True)
    tnx_no =  models.CharField(max_length = 10,editable=False,null=True,blank=True)    
    package_id = models.ForeignKey(Package, on_delete=models.CASCADE)
    #sponsor_id = models.ForeignKey(Sponsor, on_delete=models.CASCADE)
    agent_id = models.ForeignKey("agent.Agent", on_delete=models.CASCADE,null=True,blank=True)
    user_position_status = models.ForeignKey(UsePositionStatus,null=True,blank=True, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    birth_date = models.DateTimeField(null=True,blank=True)

    current_wallet = models.FloatField(default=0)
    registration_wallet = models.FloatField(default=0)
    sponsor_wallet = models.FloatField(default=0)
    founder_wallet = models.FloatField(default=0)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(null=True,blank=True)
    def __str__(self):
        return self.full_name