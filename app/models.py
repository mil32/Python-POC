from django.db import models
from django.contrib.auth.models import User


class Host(User):
    pass

    class Meta:
        verbose_name_plural = "Propietario de Inmueble"



class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Property(models.Model):
    max_pax = models.IntegerField()
    price = models.IntegerField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Booking(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.FloatField()
    guest = models.CharField(max_length=100)

    def __str__(self):
        return self.guest
