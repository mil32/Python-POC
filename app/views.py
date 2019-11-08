from django.shortcuts import render
from django.http import HttpResponse
from app.models import Property, City
from pprint import pprint


def index(request):
    properties = Property.objects.all()
    cities = City.objects.all()
    context = {
        'properties' : properties,
        'cities' : cities,
    }
    return render(request, 'app/index.html', context)


def property(request):
    test = "Property"
    context = {
        'variable': test,
    }
    return render(request, 'app/property.html', context)


def booking(request):
    test = "Booking"
    context = {
        'variable': test,
    }
    return render(request, 'app/booking.html', context)

    
