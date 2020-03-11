from django.shortcuts import render
from .models import Cat
import requests
import secrets
from random import randint


def home(request):
    context = {
        'cats': Cat.objects.all()
    }
    return render(request, 'cats/home.html', context)


def about(request):
    return render(request, 'cats/about.html', {'title': 'About'})


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
        {'latitude':37.6945,'longitude':-122.074},
        {'latitude':37.5922,'longitude':-122.075},
        {'latitude':37.6314,'longitude':-122.075},
        {'latitude':37.3824,'longitude':-122.077},
        {'latitude':37.3829,'longitude':-122.078},
        {'latitude':37.4142,'longitude':-122.078},
        {'latitude':37.6652,'longitude':-122.078},
        {'latitude':37.6659,'longitude':-122.078},
        {'latitude':37.402,'longitude':-122.079},
        {'latitude':37.6313,'longitude':-122.079},
        {'latitude':37.6669,'longitude':-122.079},
        {'latitude':37.6703,'longitude':-122.08},
        {'latitude':37.6678,'longitude':-122.082},
        {'latitude':37.6954,'longitude':-122.082},
        {'latitude':37.3852,'longitude':-122.083},
        {'latitude':37.6945,'longitude':-122.085},
        {'latitude':37.3866,'longitude':-122.086},
        {'latitude':37.6512,'longitude':-122.09},
        {'latitude':37.6837,'longitude':-122.09},
        {'latitude':37.6922,'longitude':-122.09},
        {'latitude':37.6924,'longitude':-122.09},
        {'latitude':37.4198,'longitude':-122.093},
        {'latitude':37.6246,'longitude':-122.093},
        {'latitude':37.4207,'longitude':-122.094},
        {'latitude':37.9591,'longitude':-122.094},
        {'latitude':37.6316,'longitude':-122.095},
        {'latitude':37.391,'longitude':-122.096},
        {'latitude':37.6295,'longitude':-122.096},
        {'latitude':37.3938,'longitude':-122.098},
        {'latitude':37.4217,'longitude':-122.1},
        {'latitude':37.6857,'longitude':-122.1},
        {'latitude':37.9931,'longitude':-122.1},
        {'latitude':37.638,'longitude':-122.101},
        {'latitude':37.654,'longitude':-122.101},
        {'latitude':37.994,'longitude':-122.101},
        {'latitude':37.422,'longitude':-122.102},
        {'latitude':37.6439,'longitude':-122.104},
        {'latitude':37.6878,'longitude':-122.104},
        {'latitude':37.397,'longitude':-122.105},
        {'latitude':37.6545,'longitude':-122.105},
        {'latitude':37.6469,'longitude':-122.106},
        {'latitude':37.6665,'longitude':-122.106},
        {'latitude':37.9943,'longitude':-122.107},
        {'latitude':37.3984,'longitude':-122.109},
        {'latitude':37.4001,'longitude':-122.109},
        {'latitude':37.4006,'longitude':-122.109},
        {'latitude':37.8935,'longitude':-122.11},
        {'latitude':37.9959,'longitude':-122.11},
        {'latitude':37.6933,'longitude':-122.111},
        {'latitude':37.4019,'longitude':-122.113},
        {'latitude':37.8927,'longitude':-122.113},
        {'latitude':37.8925,'longitude':-122.114},
        {'latitude':37.8924,'longitude':-122.116},
        {'latitude':37.9954,'longitude':-122.117},
        {'latitude':37.6656,'longitude':-122.118},
        {'latitude':37.653,'longitude':-122.119},
        {'latitude':37.9942,'longitude':-122.119},
        {'latitude':37.6712,'longitude':-122.121},
        {'latitude':37.6719,'longitude':-122.122},
        {'latitude':37.6868,'longitude':-122.122},
        {'latitude':37.6747,'longitude':-122.123},
        {'latitude':37.6744,'longitude':-122.124},
        {'latitude':37.8582,'longitude':-122.124},
        {'latitude':37.6769,'longitude':-122.125},
        {'latitude':37.6863,'longitude':-122.125},
        {'latitude':37.8631,'longitude':-122.125},
        {'latitude':37.7031,'longitude':-122.127},
        {'latitude':37.7053,'longitude':-122.128},
        {'latitude':37.8345,'longitude':-122.129},
        {'latitude':37.4172,'longitude':-122.13},
        {'latitude':37.6874,'longitude':-122.13},
        {'latitude':37.699,'longitude':-122.13},
        {'latitude':37.7015,'longitude':-122.13},
        {'latitude':37.4174,'longitude':-122.131},
        {'latitude':37.995,'longitude':-122.132},
        {'latitude':37.7079,'longitude':-122.133},
        {'latitude':37.457,'longitude':-122.134},
        {'latitude':37.4579,'longitude':-122.137},
        {'latitude':37.6807,'longitude':-122.138},
        {'latitude':37.4213,'longitude':-122.139},
        {'latitude':37.6867,'longitude':-122.139},
        {'latitude':37.4719,'longitude':-122.14},
        {'latitude':37.4257,'longitude':-122.147},
        {'latitude':37.4799,'longitude':-122.151},
        {'latitude':37.7414,'longitude':-122.151},
        {'latitude':37.7234,'longitude':-122.154},
        {'latitude':37.7246,'longitude':-122.157},
        {'latitude':37.7145,'longitude':-122.158},
        {'latitude':37.713,'longitude':-122.159},
        {'latitude':37.7235,'longitude':-122.161},
        {'latitude':37.4426,'longitude':-122.17},
        {'latitude':37.7088,'longitude':-122.171},
        {'latitude':37.7441,'longitude':-122.171},
        {'latitude':37.7447,'longitude':-122.171},
        {'latitude':37.7662,'longitude':-122.176},
        {'latitude':37.7048,'longitude':-122.178},
        {'latitude':37.7666,'longitude':-122.178},
        {'latitude':37.7676,'longitude':-122.179},
        {'latitude':37.718,'longitude':-122.181},
        {'latitude':37.7181,'longitude':-122.181}   
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

    # cat1 = Cat(name='Brent',photo='blank',age=5,breed='human',latitude=0,longitude=0)
    # cat1.save()
