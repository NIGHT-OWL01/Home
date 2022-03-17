from django.contrib import admin
from .models import room,message
# Register your models here.

@admin.register(room)
class RoomAdmin(admin.ModelAdmin):
    list_display=['id','title']

@admin.register(message)
class RoomAdmin(admin.ModelAdmin):
    list_display=['id','value','user']