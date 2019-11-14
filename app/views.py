from django.shortcuts import render
from django.http import HttpResponse
from app.models import Property, City


def index(request):
    properties = Property.objects.all()
    cities = City.objects.all()
    city = request.POST.get('cities')
    price_from = request.POST.get('price_from')
    price_to = request.POST.get('price_to')
    max_pax = request.POST.get('max_pax',None)
    if request.method == 'POST':
        properties = Property.objects.filter(city=city)
        if (max_pax != ''):
            properties = properties.filter(max_pax=max_pax)
        if (price_from != ''):
            properties = properties.filter(price__gte=price_from)
        if (price_to != ''):
            properties = properties.filter(price__lte=price_to)
    context = {
        'properties' : properties,
        'cities' : cities,
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
