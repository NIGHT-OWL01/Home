from rest_framework import serializers

from .models import Doctor,Speciality

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id','location', 'name', 'address']