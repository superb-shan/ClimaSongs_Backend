import requests

def __init__():
    print("Weather Called")

def getWeather(locationData):
    print("In Weather", locationData, locationData["latitude"], locationData['longitude'])

    url = f'http://api.openweathermap.org/data/2.5/weather?lat={locationData["latitude"]}&lon={locationData['longitude']}&appid=462549756bfa91a757b458bf854e14f7&units=metric'

    res = requests.get(url)
    data = res.json()

    # print(data)
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    wind = data['wind']['speed']
    description = data['weather'][0]['description']
    temp = data['main']['temp']
    name = data['name']

    # print('Temperature:',temp,'°C')
    # print('Wind:',wind)
    # print('Pressure: ',pressure)
    # print('Humidity: ',humidity)
    # print('Description:', description)
    # print('Name:', name)
    return ({ 'humidity': humidity, 'pressure': pressure, 'wind': wind, 'description': description, 'temp': temp, 'name': name })