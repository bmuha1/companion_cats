from django.shortcuts import render

cats = [
    {
        'id': 1,
        'photo': 'https://i.imgur.com/RSXl1iN.jpg',
        'name': 'Gary',
        'age': 9,
        'breed': 'American Shorthair',
        'color': 'orange'
    },
    {
        'id': 2,
        'photo': 'https://i.imgur.com/M5fQpjG.jpg',
        'name': 'Thor',
        'age': 4,
        'breed': 'Unknown',
        'color': 'black, white'
    }
]


def home(request):
    context = {
        'cats': cats,
    }
    return render(request, 'cats/home.html', context)


def about(request):
    return render(request, 'cats/about.html', {'title': 'About'})
