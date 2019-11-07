from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    test = "TU VIEJA"
    context = {
        'variable': test,
    }
    return render(request, 'app/index.html', context)
