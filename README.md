<p align="center"><img src="https://i.imgur.com/9hHiH87.png" alt="Companion Cats" width=565  height=391></p>

# Companion Cats

## Introduction

All students at Holberton School are tasked with completing a capstone project at the end of the foundations year. For my project, I created Companion Cats, a platform to borrow cats built in Python utilizing various APIs. The purpose of the project is to demonstrate my ability to create a full stack web app after completing nine months of projects at Holberton. I wanted to challenge myself to create a responsive website on my own. I completed both the front end and the back end. We were given two weeks to come up with an idea and conduct research, two weeks to implement the project, and one week to create a landing page and presentation.

The site is deployed [on Heroku](https://companion-cats.herokuapp.com/).

I wrote a blog post about this project: [The Making of Companion Cats](https://medium.com/@bmuha1/the-making-of-companion-cats-3311a967b17f).

My LinkedIn page is [available here](https://www.linkedin.com/in/brentmuha/).

## Inspiration

I drew inspiration from a wide range of sources. The first is Poppy, the Holberton CPO (Chief Puppy Officer). Poppy wanders around the school, getting lots of attention from the students. Whenever I see Poppy, I take a break from my project to pet her for a few minutes. She has been very comforting and acts as our “therapy” dog.

The next source of inspiration is Wag, which bills itself as Uber for dog walking. I’ve been walking dogs on Wag for the past three years, and it’s a great way to spend some time with a variety of dogs without committing to pet ownership. I wanted to create a similar app that’s focused on cats. One day I was having a conversation with a classmate, Aalaa, and she told me about her idea for an app that lets you borrow cats. This eventually became Companion Cats.

Finally, I was inspired by my experiences with my own cat, Gary. Gary is an orange boy who loves sitting in my lap and getting his belly rubbed. When I work on my projects at home, he’s often there with me, constantly purring. I know a lot of people would love to have a pet that sits in their lap, but it’s not always viable to own one yourself.

## Architecture

<p align="center"><img src="https://miro.medium.com/max/884/0*qAqiRjQws3jTFFjW" alt="Architecture"></p>

## Technology

<p align="center"><img src="https://miro.medium.com/max/5760/1*SPi_MyDuBhk0Qv8ysKM3wQ.png" alt="Architecture" width=576  height=360></p>

The bulk of the site is built in Python, using Django. The front end is written in HTML, CSS, and JavaScript. I used Bootstrap because I wanted a responsive site that looks simple and clean. Jinja is used in the Django templates to display the dynamically generated data. I used PostgreSQL for my database, populated with Cat objects. I used the Cat API to get cat breeds and photos, and I assigned each cat GPS coordinates from Fast Food Maps. Directions from the user to the cat are generated using the Google Maps API. Finally, the site is deployed on Heroku, using Gunicorn.

## Installation

Companion Cats does not need to be installed. Simply browse the site at https://companion-cats.herokuapp.com/.

## Usage

<img src="https://i.imgur.com/GoAuqa7.png" alt="Find a Cat" width=576  height=360>

### Find a Cat

Find just the cat you're looking for! Cats can be filtered by age and breed.
  
<img src="https://i.imgur.com/lVJtjMx.png" alt="All Cats" width=576  height=360>

### All Cats

Browse our entire collection of cats available. 1300+ cats located all over the San Francisco Bay Area!

<img src="https://i.imgur.com/SWwg0o9.png" alt="Borrow a Cat" width=576  height=360>

### Borrow a Cat

Once you've found the perfect cat for you, get directions and go pick it up!

## Author

[Brent Muha](https://github.com/bmuha1)

My name is Brent Muha and I created Companion Cats. I’m a former elementary school teacher transitioning into software engineering. I love problem solving and collaborating with others. This site is my capstone project at Holberton School, and I am pursuing opportunities as a full stack web developer with a focus on back end.

## Related Projects

[Wag](https://wagwalking.com)

[Puppr](https://puppr.best)

## Licensing

MIT License
