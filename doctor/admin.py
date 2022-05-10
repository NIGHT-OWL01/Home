from django.contrib import admin
from .models import Doctor,Speciality
from django.contrib.gis.admin import OSMGeoAdmin
# Register your models here.

@admin.register(Doctor)
class DoctorAdmin(OSMGeoAdmin):
    list_display=['id','name','location','experience','address']

@admin.register(Speciality)
class DoctorAdmin(OSMGeoAdmin):
    list_display=['id','name']