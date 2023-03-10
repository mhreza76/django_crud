from django.http import HttpResponse
from django.shortcuts import render
from service.models import Service

def aboutUs(request):
    return HttpResponse("Welcome to django")

def courseDetails(request, course_id):
    return HttpResponse(course_id)

def homePage(request):
    serviceData = Service.objects.all().order_by('-id')[:3]
    data = {
        'serviceData': serviceData,
        'title':'Home Page',
        'clist':['PHP', 'Python', 'Django'],
        'numbers':[10, 20, 30, 40, 50],
        'student_details':[
            {'name':'reza', 'phone':"01633613553"},
            {'name':'hasib', 'phone':"01790984531"},
        ]
    }
    return render(request, "index.html", data)