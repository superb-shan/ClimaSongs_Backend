import json
import random
from rest_framework import status
from rest_framework.response import Response
from django.core import serializers
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import Location, WeatherData, Songs
from .serializers import LocationSerializer, WeatherDataSerializer
from .API.Weather import getWeather
from .API.Spotify import getSongInfo
from django.forms.models import model_to_dict

class LocationView(APIView):
    def post(self, request, format=None):
        serializer = LocationSerializer(data=request.data)
        print(getWeather(request.data))
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WeatherDataView(APIView):
    def get(self, request, format=None):

        weather_data = getWeather({'latitude': Location.objects.latest('pk').latitude, 'longitude': Location.objects.latest('pk').longitude})
        
        weather = WeatherData(humidity = weather_data['humidity'],pressure= weather_data['pressure'], wind= weather_data['wind'], description= weather_data['description'],temp= weather_data['temp'], name= weather_data['name'])
        weather.save()

        return Response(weather_data)

class SongsDataView(APIView):
    def map_weather_condition(self, condition):
        if condition in ['mist', 'haze', 'fog']:
            return 'mist'
        elif condition in ['scattered clouds', 'few clouds']:
            return 'cloudy'
        elif condition in ['light rain', 'thunderstorm']:
            return 'thunderstorm'
        else:
            return 'clear sky'

    def get(self, request, format=None):
        songs = list(Songs.objects.filter(climate=self.map_weather_condition(WeatherData.objects.latest('pk').description)))
        random.shuffle(songs)
        serialized_songs = serializers.serialize('json', songs)
        songs_data = json.loads(serialized_songs)
        song_names = [entry['fields']['song_name'] for entry in songs_data]

        response_data = {'data': []}

        for song in song_names:
            response_data["data"].append({"name": song, "search_results": getSongInfo(song)})

        return JsonResponse(response_data, safe=False)
