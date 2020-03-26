from django.db import models
from django import forms


class Cat(models.Model):
    """
    Cat object, contains the following attributes
    name: string
    photo: string containing a URL
    age: int
    breed: string
    latitude: float
    longitude: float
    available: bool, default is True
    """
    name = models.CharField(max_length=20)
    photo = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=8, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    available = models.BooleanField(default=True)

    
    def __str__(self):
        # Return the name of the Cat
        return self.name
