from django.shortcuts import render
from .models import Collection_items, Dairy,Contact,Collection
from django.http import HttpResponse,JsonResponse
from .serializers import ContactSerializer, DairySerializer, UserSerializer,CollectionSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate,login
from datetime import timedelta
from django.middleware import csrf
from django.contrib.auth.models import User

from apps import serializers
# Create your views here.
@api_view(['GET','POST'])
def collections(request):
    if request.method=='GET':
        collection_list=Collection.objects.all()
        serializer=CollectionSerializer(collection_list,many=True)
        return Response(serializer.data)
    if request.method=='POST':
        print('POST of collection')
        r=request.data
        print(request.user.id)
        if 'token' in request.headers:
            title=request.data['title']
            user=request.data['user']
            user=User.objects.get(id=user)
            c=Collection.objects.create(title=title,user=user)
            print(title,user)
            return Response('user authenticated')
        return Response('token not found')


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

@api_view(['GET','POST'])
def user_auth(request):
    u_name=request.data['username']
    u_pass=request.data['password']
    data = request.data
    response = Response() 
    user=authenticate(username=u_name,password=u_pass)
    if user:
        user=User.objects.filter(username=u_name)
        serializer=UserSerializer(user,many=True)
        user=User.objects.get(username=u_name)
        token=get_tokens_for_user(user)
        cookie_max_age = 3600 * 24 * 14 # 14 days
        response.set_cookie(
            key = 'access_token', 
            value = token,
            expires = cookie_max_age,
            secure = False,
            httponly = True,
            samesite = 'Lax'
                )
        response.set_cookie('my_cookie', 'Product Cart', max_age=cookie_max_age)
        login(request,user)
        print(response)
        response.data = {"Success" : "Login successfully","data":token}
        print('resdponse data:',response.data)        
        return response
        #return Response({'User logged in':token})
    return Response('no data',status=status.HTTP_406_NOT_ACCEPTABLE)
    


@api_view(['GET'])
def cookies(request):
    if request.method == 'GET':
        if 'cookie' in request.COOKIES:
            value = request.COOKIES['cookie']
            response = HttpResponse('Works')
            return response
        else:
            response = HttpResponse('Does Not Works')
            response.set_cookie('token', 'MY Token')
            return response

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
        dairy_list=Dairy.objects.all()
        serializer=DairySerializer(dairy_list, many=True)
        return Response({'dairy items':serializer.data})
    if request.method=='POST':
        return Response({'msg':'POST dairy'})

#######################################################################################################
def home(request):
    if request.method=='GET':
        collection_item_list=Collection_items.objects.all()
        collection_list=Collection.objects.prefetch_related('collection_items_set')
        print(collection_list)
        ctx={'collections':collection_list,'collection_items':collection_item_list}
        return render(request, 'home.html',ctx)