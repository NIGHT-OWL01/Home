from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Motor(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=250,blank=True,null=True)
    active=models.BooleanField(default=False,blank=True,null=True)
    owner=models.ForeignKey(User,on_delete=models.DO_NOTHING,blank=True,null=True)