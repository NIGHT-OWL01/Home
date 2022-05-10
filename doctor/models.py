from django.contrib.gis.db import models
# Create your models here.



class Speciality(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
class Doctor(models.Model):
    name=models.CharField(max_length=100)
    experience=models.CharField(max_length=100,blank=True,null=True)
    location=models.PointField()
    address=models.CharField(max_length=100, blank=True, null=True)
    speciality=models.ForeignKey(Speciality, on_delete=models.DO_NOTHING,null=True)

