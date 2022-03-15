from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
# Create your views here.

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'invalid credentials')
            return redirect('login')
    else:    
        return render(request, 'account/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def register(requst):
    if requst.method=='POST':
        first_name=requst.POST['first_name']
        last_name=requst.POST['last_name']
        username=requst.POST['username']
        email=requst.POST['email']
        password1=requst.POST['password1']
        password2=requst.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(requst, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(requst, 'Email Taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('user created!')
                return redirect('login')
        else:
            print('password not match ')
        return redirect('register')
    else:    
        return render(requst, 'account/register.html')