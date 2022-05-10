from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Contact(models.Model):
    name =models.CharField(max_length=50)
    phone_number =models.CharField(max_length=10)
    address =models.CharField(max_length=100,blank=True)


class Dairy(models.Model):
    sold=models.IntegerField()
    price=models.IntegerField()

class Collection(models.Model):
    title=models.CharField(max_length=100, unique=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
class Collection_items(models.Model):
    name=models.CharField(max_length=60)
    quantity=models.CharField(max_length=15,null=True, blank=True)
    collection=models.ForeignKey(Collection, on_delete=models.DO_NOTHING,null=True, blank=True)
