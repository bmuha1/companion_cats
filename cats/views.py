from django.shortcuts import render
from .models import Cat
import requests
import secrets
from random import randint
from math import sin, cos, radians, degrees, acos


def home(request):
    return render(request, 'cats/home.html')


def all(request):
    cats = Cat.objects.all()
    for cat in cats:
        cat.distance = calc_dist(37.781975, -122.407448, float(cat.latitude), float(cat.longitude))
    context = {
        'cats': cats,
        'title': 'All Cats'
    }

    return render(request, 'cats/display.html', context)


def find(request):
    breeds = []
    cats = Cat.objects.all()
    for cat in cats:
        cat.distance = calc_dist(37.781975, -122.407448, float(cat.latitude), float(cat.longitude))
        if cat.age <= 2:
            cat.age_range = '0'
        elif cat.age >= 3 and cat.age <= 5:
            cat.age_range = '3'
        elif cat.age >= 6 and cat.age <= 9:
            cat.age_range = '6'
        elif cat.age >= 10 and cat.age <= 12:
            cat.age_range = '10'
        elif cat.age >= 13 and cat.age <= 16:
            cat.age_range = '13'
        else:
            cat.age_range = '17'
        breeds.append(cat.breed)
    breeds = list(dict.fromkeys(breeds))
    breeds.sort()
    context = {
        'breeds': breeds,
        'cats': cats,
        'title': 'Find a Cat'
    }
    return render(request, 'cats/find.html', context)


def cat(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    cat.distance = calc_dist(37.781975, -122.407448, float(cat.latitude), float(cat.longitude))
    if cat.distance > 1:
        cat.mode = 'driving'
    else:
        cat.mode = 'walking'
    context = {
        'cat': cat,
        'title': 'Borrow a Cat'
    }
    return render(request, 'cats/cat.html', context)


def about(request):
    return render(request, 'cats/about.html', {'title': 'About'})


""" This function is taken from here: https://stackoverflow.com/questions/4716017/django-how-can-i-find-the-distance-between-two-locations/4716690#4716690 """
def calc_dist(lat_a, long_a, lat_b, long_b):
    lat_a = radians(lat_a)
    lat_b = radians(lat_b)
    long_diff = radians(long_a - long_b)
    distance = (sin(lat_a) * sin(lat_b) +
                cos(lat_a) * cos(lat_b) * cos(long_diff))
    resToMile = degrees(acos(distance)) * 69.09
    # resToMt = resToMile / 0.00062137119223733
    return resToMile


def random(request):
    types = []
    
    breeds = requests.get('https://api.thecatapi.com/v1/breeds').json()
    # breeds = [{'id': 'abys'}]

    for breed in breeds:
        cat = requests.get('https://api.thecatapi.com/v1/images/search?breed_ids=' + breed.get('id')).json()[0]
        # cat = cat.get('url')
        types.append(cat)

    context = {
        'cats': types
    }
    return render(request, 'cats/random.html', context)


def add(request):
    types = []

    coordinates = [
        {'latitude':37.7051,'longitude':-121.721},
        {'latitude':37.9978,'longitude':-121.721},
        {'latitude':37.7061,'longitude':-121.723},
        {'latitude':37.7092,'longitude':-121.724},
        {'latitude':37.7117,'longitude':-121.724},
        {'latitude':37.7183,'longitude':-121.724},
        {'latitude':37.9979,'longitude':-121.731},
        {'latitude':37.6966,'longitude':-121.735},
        {'latitude':37.9253,'longitude':-121.735},
        {'latitude':37.9617,'longitude':-121.743}

    ]

    breeds = requests.get('https://api.thecatapi.com/v1/breeds').json()
    # breeds = [{'id': 'abys'}]

    names = [
        'Aalaa',
        'Adekunle',
        'Afa',
        'Ahad',
        'Akeem',
        'Alex',
        'Alexa',
        'Alexandre',
        'Alexandro',
        'Alexis',
        'Alia',
        'Allison',
        'Amadriel',
        'Amber',
        'Amy',
        'Andres',
        'Andrew',
        'Angie',
        'Anne',
        'Anne-Sophie',
        'Anoop',
        'Anthony',
        'Ariana',
        'Arik',
        'Arthur',
        'Artur',
        'Athena',
        'Banu',
        'Becky',
        'Ben',
        'Bennett',
        'Bianca',
        'Bilal',
        'Binita',
        'Brendan',
        'Brennan',
        'Brent',
        'Bryan',
        'CaNese',
        'Cameron',
        'Carole',
        'Carrie',
        'Chandler',
        'Charles',
        'Christine',
        'Christopher',
        'Colton',
        'Constance',
        'Corbin',
        'Cuong',
        'Cynthia',
        'Damon',
        'Daniel',
        'Darnell',
        'David',
        'Debora',
        'Dennis',
        'Derek',
        'Derric',
        'Derrick',
        'Diva',
        'Domitille',
        'Dora',
        'Drew',
        'Edward',
        'Elaine',
        'Electra',
        'Elena',
        'Elizabeth',
        'Eric',
        'Erika',
        'Essence',
        'Ethan',
        'Evan',
        'Evdokiya',
        'Farrukh',
        'Felicia',
        'Fernando',
        'Florian',
        'Gaoqing',
        'George',
        'Germaine',
        'Grant',
        'Grayson',
        'Gregory',
        'Guillaume',
        'Hanh',
        'Heindrick',
        'Hemant',
        'Henry',
        'Holden',
        'Hongtu',
        'Hunter',
        'Ian',
        'Isaac',
        'Isaiah',
        'Jack',
        'Jacob',
        'James',
        'Jannis',
        'Jared',
        'Jason',
        'Jeffrey',
        'Jennifer',
        'Jerel',
        'Jeremy',
        'Jesse',
        'Jessica',
        'Jian',
        'Jianqin',
        'Jimmy',
        'Jinji',
        'Joan',
        'John',
        'Joseph',
        'Joshua',
        'Julien',
        'Julija',
        'Jun',
        'Juno',
        'Justin',
        'Katya',
        'Kenneth',
        'Kevan',
        'Kevin',
        'Kimberly',
        'Kiren',
        'Koome',
        'Kristen',
        'Kristine',
        'Kyle',
        'Laura',
        'Laurence',
        'Lee',
        'Leine',
        'Lindsey',
        'Lisa',
        'Madison',
        'Marc',
        'Marco',
        'Marine',
        'Marius',
        'Martin',
        'Mason',
        'Max',
        'Megha',
        'Michelle',
        'Mikaela',
        'Minhhuy',
        'Miranda',
        'Mitali',
        'Naomi',
        'Nathan',
        'Nehal',
        'Nga',
        'Niat',
        'Nicholas',
        'Nick',
        'Ntuj',
        'Olatope',
        'Omar',
        'Patrick',
        'Paul',
        'Pauline',
        'Peter',
        'Philip',
        'Phu',
        'Pierre',
        'Ramandeep',
        'Rashaad',
        'Raudo',
        'Rene',
        'Richard',
        'Rick',
        'Robert',
        'Rona',
        'Rui',
        'Ryuichi',
        'Samie',
        'Samuel',
        'Scout',
        'Sergii',
        'Sergio',
        'Shoji',
        'Sidney',
        'Sneha',
        'Sofia',
        'Sonia',
        'Sophie',
        'Spencer',
        'Sravanthi',
        'Stephen',
        'Steven',
        'Sumin',
        'Swati',
        'Sylvain',
        'Tabitha',
        'Tammy',
        'Tanya',
        'Tasneem',
        'Thomas',
        'Tiffany',
        'Tim',
        'Timothy',
        'Travis',
        'Trevor',
        'Tu',
        'Van',
        'Vasudha',
        'Veronica',
        'Victor',
        'Walton',
        'Wendy',
        'Yannis',
        'Yashar',
        'Yunju',
        'Zachary'
    ]

    for c in coordinates:
        breed = secrets.choice(breeds)
        cat = requests.get('https://api.thecatapi.com/v1/images/search?breed_ids=' + breed.get('id')).json()[0]
        cat['breed'] = cat['breeds'][0]['name']
        cat['latitude'] = c['latitude']
        cat['longitude'] = c['longitude']
        cat['age'] = randint(0,20)
        cat['name'] = secrets.choice(names)
        cat1 = Cat(name=cat['name'], photo=cat['url'], breed=cat['breed'], age=cat['age'], latitude=cat['latitude'], longitude=cat['longitude'])
        cat1.save()
        types.append(cat)

    context = {
        'cats': types,
    }
    return render(request, 'cats/random.html', context)
