from django.shortcuts import redirect, render
from .models import Motor
from django.views.generic.edit import UpdateView
# Create your views here.

def home(request):
    motors=Motor.objects.all()
    ctx={'motors':motors}
    return render(request, 'sheti/sheti_index.html',ctx)

def motors(request):
    if request.method=='GET':
        print('get called')
        return render(request, 'sheti/add_motor.html')
    if request.method=='POST':
        print('post called')
        name=request.POST['name']
        address=request.POST['address']
        active=request.POST.get('active','False')
        if active=='on':
            active='True'
        motor=Motor(name=name,address=address,active=active,owner=request.user)
        motor.save()
        print(name,address,active)
        return redirect('sheti_home')

class MotorUpdateView(UpdateView):
    model = Motor
    fields = ['owner']
    template_name= 'sheti/update_motor.html'