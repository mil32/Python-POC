from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    test = "TU VIEJA"
    context = {
        'variable': test,
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

    
