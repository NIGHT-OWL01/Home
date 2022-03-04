from django.db import models

# Create your models here.
class Contact(models.Model):
    name =models.CharField(max_length=50)
    phone_number =models.CharField(max_length=10)
    address =models.CharField(max_length=100,blank=True)

class Dairy(models.Model):
    sold=models.IntegerField()
    price=models.IntegerField()
