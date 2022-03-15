from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def chat(request):
    u=request.user.username
    ctx={'username':u}
    return render(request, 'chat/home.html',ctx)