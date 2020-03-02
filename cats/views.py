from django.shortcuts import render


def home(request):
    return render(request, 'cats/home.html')


def about(request):
    return render(request, 'cats/about.html')