from django.shortcuts import render
from .models import Cat
import requests
import secrets
from random import randint
from math import sin, cos, radians, degrees, acos


def home(request):
    return render(request, 'cats/home.html')


def find(request):
    breeds = []
    all = Cat.objects.all()
    for cat in all:
        breeds.append(cat.breed)
    breeds = list(dict.fromkeys(breeds))
    breeds.sort()
    context = {
        'breeds': breeds
    }
    return render(request, 'cats/find.html', context)


def all(request):
    context = {
        'cats': Cat.objects.all()
    }
    return render(request, 'cats/home.html', context)


def cat(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    cat.distance = calc_dist(37.781975, -122.407448, float(cat.latitude), float(cat.longitude))
    context = {
        'cat': cat
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
    resToMt = resToMile / 0.00062137119223733
    return resToMt


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
        {'latitude':37.7997,'longitude':-122.436},
        {'latitude':37.6565,'longitude':-122.437},
        {'latitude':37.722,'longitude':-122.437},
        {'latitude':37.7854,'longitude':-122.437},
        {'latitude':37.7448,'longitude':-122.44},
        {'latitude':37.7132,'longitude':-122.444},
        {'latitude':37.6662,'longitude':-122.451},
        {'latitude':37.6665,'longitude':-122.452},
        {'latitude':37.6434,'longitude':-122.453},
        {'latitude':37.7687,'longitude':-122.453},
        {'latitude':37.7236,'longitude':-122.455},
        {'latitude':37.7813,'longitude':-122.461},
        {'latitude':37.7813,'longitude':-122.464},
        {'latitude':37.7813,'longitude':-122.464},
        {'latitude':37.6873,'longitude':-122.465},
        {'latitude':37.6932,'longitude':-122.465},
        {'latitude':37.6937,'longitude':-122.465},
        {'latitude':37.7265,'longitude':-122.465},
        {'latitude':37.7265,'longitude':-122.465},
        {'latitude':37.6768,'longitude':-122.466},
        {'latitude':37.7635,'longitude':-122.466},
        {'latitude':37.6715,'longitude':-122.468},
        {'latitude':37.669,'longitude':-122.469},
        {'latitude':37.6702,'longitude':-122.469},
        {'latitude':37.7806,'longitude':-122.469},
        {'latitude':37.6709,'longitude':-122.47},
        {'latitude':37.688,'longitude':-122.471},
        {'latitude':37.6922,'longitude':-122.471},
        {'latitude':37.6923,'longitude':-122.471},
        {'latitude':37.7268,'longitude':-122.476},
        {'latitude':37.7431,'longitude':-122.478},
        {'latitude':37.7431,'longitude':-122.478},
        {'latitude':37.7634,'longitude':-122.478},
        {'latitude':37.7634,'longitude':-122.478},
        {'latitude':37.7341,'longitude':-122.487},
        {'latitude':37.6811,'longitude':-122.488},
        {'latitude':37.6831,'longitude':-122.488},
        {'latitude':37.6831,'longitude':-122.488},
        {'latitude':37.6498,'longitude':-122.49},
        {'latitude':37.6522,'longitude':-122.492},
        {'latitude':37.6995,'longitude':-122.492},
        {'latitude':37.6097,'longitude':-122.493},
        {'latitude':37.5944,'longitude':-122.502},
        {'latitude':37.5971,'longitude':-122.502},
        {'latitude':37.961,'longitude':-122.505},
        {'latitude':37.9575,'longitude':-122.508},
        {'latitude':37.8717,'longitude':-122.509},
        {'latitude':37.7746,'longitude':-122.51},
        {'latitude':37.8905,'longitude':-122.516},
        {'latitude':37.8967,'longitude':-122.516},
        {'latitude':37.926,'longitude':-122.517},
        {'latitude':37.9702,'longitude':-122.52},
        {'latitude':37.8935,'longitude':-122.531},
        {'latitude':37.8935,'longitude':-122.531},
        {'latitude':37.8958,'longitude':-122.535},
        {'latitude':37.996,'longitude':-122.535},
        {'latitude':37.9733,'longitude':-122.539},
        {'latitude':37.9758,'longitude':-122.547},
        {'latitude':37.9796,'longitude':-122.564}
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
