from django.contrib.gis.geos import Point, GEOSGeometry
from django.contrib.gis.db.models.functions import Distance
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .models import Doctor, Speciality
from .serializers import DoctorSerializer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.response import Response
#from django.contrib.gis.geoip2 import GeoIP2
# Create your views here.

def welcome(request):
    if request.method=='GET':
        return render(request, 'doctor/index.html')
    if request.method=='POST':
        return redirect('doctor_search',city='pune')
    

def doctor_registrater(request):
    return HttpResponse("Welcome to reg")
def doctor_search(request):
    latitude = float(request.GET.get('lat', '0'))
    longitude = float(request.GET.get('long', '0'))
    city = request.GET.get('city', '0')
    user_location = Point(longitude, latitude, srid=4326)

    if latitude !=0 and longitude !='0':
        doctor_list=Doctor.objects.annotate(distance=Distance("location", user_location)).order_by("distance")
    else:
        doctor_list=Doctor.objects.filter(city__icontains=city)
    context={'doctor_list':doctor_list}
    return render(request,'doctor/doctor_search.html',context)

























    '''
    page = request.GET.get('page', 1)
    paginator = Paginator(doctor_list, 5)
    try:
        doctor_list = paginator.page(page)
    except PageNotAnInteger:
        doctor_list = paginator.page(1)
    except EmptyPage:
        response = Response("Page out of range", 400)
        response['Page-Count'] = paginator.num_pages
        return response
    serializer = DoctorSerializer(doctor_list, many=True)
    response = JsonResponse(serializer.data, safe=False)
    response['Page-Count'] = paginator.num_pages
    return response
    '''



    '''
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    
    device_type = ""
    browser_type = ""
    browser_version = ""
    os_type = ""
    os_version = ""
    if request.user_agent.is_mobile:
        device_type = "Mobile"
    if request.user_agent.is_tablet:
        device_type = "Tablet"
    if request.user_agent.is_pc:
        device_type = "PC"
    
    browser_type = request.user_agent.browser.family
    browser_version = request.user_agent.browser.version_string
    os_type = request.user_agent.os.family
    os_version = request.user_agent.os.version_string
    print(ip)
    g = GeoIP2()
    location = g.city(ip)
    location_country = location["country_name"]
    location_city = location["city"]
    context = {
        "ip": ip,
        "device_type": device_type,
        "browser_type": browser_type,
        "browser_version": browser_version,
        "os_type":os_type,
        "os_version":os_version,
        "location_country": location_country,
        "location_city": location_city,
        'doctor_list':doctor_list
    }
    '''