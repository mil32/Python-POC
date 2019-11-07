from django.contrib import admin
from .models import Host, City, Property, Booking

admin.site.register(Host)
admin.site.register(City)
admin.site.register(Property)
admin.site.register(Booking)
