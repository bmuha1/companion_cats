from django.db import models


class Cat(models.Model):
    name = models.CharField(max_length=20)
    photo = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=8, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
