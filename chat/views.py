from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import room,message
# Create your views here.


def chat(request):
    if request.method=='POST':
        name=request.POST['room']
        if room.objects.filter(title=name).exists():
            print('room exists')
        return redirect('chat')
    else:
        u=request.user.username
        ctx={'username':u}
        return render(request, 'chat/home.html',ctx)