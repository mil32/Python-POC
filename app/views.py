from django.shortcuts import render
from django.http import HttpResponse
from .models import Property


def index(request):
    test = "TU VIEJA"
    context = {
        'variable': test,
    }
    return render(request, 'app/index.html', context)


def property(request, property_id):
    guest = request.POST.get('guest')
    prop = Property.objects.get(id=property_id)
    context = {
        'property': prop,
        'guest': guest
    }
    return render(request, 'app/property.html', context)
