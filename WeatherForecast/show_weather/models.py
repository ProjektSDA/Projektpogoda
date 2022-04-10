from django.contrib.auth.models import User
from django.db import models
from django.db.models import UniqueConstraint


class Weather(models.Model):
    location = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=20)
    temperature = models.IntegerField()
    precipitation = models.IntegerField()
    pressure = models.IntegerField()
    wind_direction = models.CharField(max_length=10)
    wind_speed = models.IntegerField()
    humidity = models.IntegerField()

class Favourite(models.Model):
    location= models.CharField(max_length=30)
    latitude=models.FloatField()
    longitude=models.FloatField()
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name='favourites')

    def __str__(self):
        return f"{self.user} favourite location : {self.location}"

    class Meta:
        constraints = [UniqueConstraint(fields=['latitude', 'longitude'], name='unique coordinates')]
