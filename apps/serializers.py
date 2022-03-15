from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
class ContactSerializer(serializers.Serializer):
    class Meta:
        model=Contact
        fields=['name','phone_number','address']

class DairySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dairy
        fields = ['id', 'price', 'sold']


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'user']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','password']