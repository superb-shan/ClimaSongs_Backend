from django.urls import path
from .views import LocationView, WeatherDataView, SongsDataView


urlpatterns = [
    path("location/", LocationView.as_view(), name="location"),
    path('weather/', WeatherDataView.as_view(), name='weather'),
    path('songs/', SongsDataView.as_view(), name='songs'),

]
