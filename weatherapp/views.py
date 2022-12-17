from django.shortcuts import render
import datetime 
import requests

# Create your views here.

def index(request):

    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = "Santiago"


    api_key = "8c5da8251f46fdead30e5194fd554436" 
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city + "&units=metric"
    response = requests.get(complete_url)
    x = response.json()
    temperature = x["main"]["temp"]
    pressure = x["main"]["pressure"]
    humidity = x["main"]["humidity"]
    description = x["weather"][0]["description"] 
    day = datetime.date.today()
    icon = x["weather"][0]["icon"]

    return render(request, 'index.html', 
            {'city': city,
            'temperature':temperature,
            'pressure':pressure,
            'humidity':humidity,
            'description':description,
            'day':day,
            'icon':icon
            })