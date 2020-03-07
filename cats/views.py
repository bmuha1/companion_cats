from django.shortcuts import render
from .models import Cat


def home(request):
    context = {
        'cats': Cat.objects.all()
    }
    return render(request, 'cats/home.html', context)


def about(request):
    return render(request, 'cats/about.html', {'title': 'About'})
