from django.db import models


class Weather(models.Model):
    location = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=20)
    temperature = models.IntegerField()
    precipitation = models.IntegerField()
    pressure = models.IntegerField()
    wind_direction = models.CharField(max_length=10)
    wind_speed = models.IntegerField()
    humidity = models.IntegerField()
