from django.db import models

class Location(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

class WeatherData(models.Model):
    humidity = models.DecimalField(max_digits=15, decimal_places=2)
    pressure = models.DecimalField(max_digits=15, decimal_places=2)
    wind = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.CharField(max_length=255)
    temp = models.DecimalField(max_digits=15, decimal_places=2)
    name = models.CharField(max_length=255)

class Songs(models.Model):
    climate = models.CharField(max_length=255)
    song_name = models.CharField(max_length=255)