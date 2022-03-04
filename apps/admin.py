from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=['name','phone_number','address']

@admin.register(Dairy)
class DairyAdmin(admin.ModelAdmin):
    list_display=['id','price','sold']