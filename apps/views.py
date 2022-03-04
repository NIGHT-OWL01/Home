from django.shortcuts import render
from .models import Dairy,Contact
from django.http import HttpResponse,JsonResponse
from .serializers import ContactSerializer, DairySerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
# Create your views here.
@api_view(['GET','POST'])
def contacts(request):
    if request.method == 'GET':
        contacts_list=Contact.objects.all()
        serializer=ContactSerializer(contacts_list, many=True)
        print(contacts_list)
        print(serializer.data)
        return JsonResponse(serializer.data, safe=False)
    if request.method=='POST':
        return JsonResponse({'msg':'contacts POST'})

@api_view(['GET','POST'])
def dairy(request):
    if request.method=='GET':
        dairy_list=Dairy.objects.filter(sold__gt=20)
        serializer=DairySerializer(dairy_list, many=True)
        return Response({'dasd':serializer.data})
    if request.method=='POST':
        return Response({'msg':'POST dairy'})