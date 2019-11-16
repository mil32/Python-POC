from django.shortcuts import render
from django.http import HttpResponse
from app.models import Property, City, Booking
from datetime import datetime


def index(request):
    properties = Property.objects.all()
    cities = City.objects.all()
    city = request.POST.get('cities')
    price_from = request.POST.get('price_from')
    price_to = request.POST.get('price_to')
    max_pax = request.POST.get('max_pax', None)
    if request.method == 'POST':
        properties = Property.objects.filter(city=city)
        if (max_pax != ''):
            properties = properties.filter(max_pax=max_pax)
        if (price_from != ''):
            properties = properties.filter(price__gte=price_from)
        if (price_to != ''):
            properties = properties.filter(price__lte=price_to)
    context = {
        'properties': properties,
        'cities': cities,
    }
    return render(request, 'app/index.html', context)


def property(request, property_id):
    prop = Property.objects.get(id=property_id)
    bookings = Booking.objects.all()
    checker = None
    guest = None

    if request.method == 'POST':
        guest = request.POST.get('guest')
        start_date = request.POST.get('start_date')
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        end_date = request.POST.get('end_date')
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        price = prop.price * (end_date - start_date).days * 1.08

        if len(bookings) > 0:
            for booking in bookings:
                if (
                        booking.start_date <= start_date <= booking.end_date or booking.start_date <= end_date <= booking.end_date) or (
                        start_date <= booking.start_date and end_date >= booking.end_date):
                    checker = False
                else:
                    checker = True
        else:
            checker = True

        if checker:
            p = Booking(property=prop, start_date=start_date,
                        end_date=end_date, price=price, guest=guest)
            p.save()

    context = {
        'property': prop,
        'checker': checker,
        'guest': guest,
    }

    return render(request, 'app/property.html', context)

# def property(request, property_id):
#     guest = request.POST.get('guest')
#     prop = Property.objects.get(id=property_id)
#     context = {
#         'property': prop,
#         'guest': guest
#     }
#     return render(request, 'app/property.html', context)
