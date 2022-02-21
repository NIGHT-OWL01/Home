from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.

def contacts(request):
    if request.method == 'GET':
        contacts_list=Contact.objects.all()
        ctx={'contacts':contacts_list}
        return render(request, 'home.html',ctx)
    else:
        return HttpResponse('contacts Post')