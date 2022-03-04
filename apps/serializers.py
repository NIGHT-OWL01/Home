from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers
from .models import *
class ContactSerializer(serializers.Serializer):
    class Meta:
        model=Contact
        fields=['name','phone_number','address']

class DairySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dairy
        fields = ['id', 'price', 'sold']
        