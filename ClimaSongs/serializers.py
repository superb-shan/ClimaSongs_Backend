from rest_framework import serializers
from .models import Location, WeatherData


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ("latitude", "longitude")

class WeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        fields = ['humidity', 'pressure', 'wind', 'description', 'temp', 'name']
