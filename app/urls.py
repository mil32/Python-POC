from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('property/<int:property_id>', views.property, name='property'),
]

