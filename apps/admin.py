from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=['name','phone_number','address']

@admin.register(Dairy)
class DairyAdmin(admin.ModelAdmin):
    list_display=['id','price','sold']

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display=['id','user','title']

@admin.register(Collection_items)
class Collection_itemsAdmin(admin.ModelAdmin):
    list_display=['id','name','quantity','collection']