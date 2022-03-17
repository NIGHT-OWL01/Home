from django.db import models

# Create your models here.

class room(models.Model):
    title=models.CharField(max_length=30)


class message(models.Model):
    value=models.CharField(max_length=500)
    room=models.CharField(max_length=100)
    user=models.CharField(max_length=20)