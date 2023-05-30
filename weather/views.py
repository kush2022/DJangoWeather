from django.shortcuts import render

import urllib.request
import json



# Create your views here.
def index(request):
    if request.method == "POST":
        city = request.POST['city']
        source = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?q=" + city + '&units=metric&appid=6e5c53868f2037e7dcd565ca6a79591c')
        
        list_of_data = json.load(source)

        data = {
            "country_code": str(list_of_data['sys']['country']),
            "temp": str(list_of_data['main']['temp']),
            "pressure": str(list_of_data['main']['pressure']), 
            "humidty": str(list_of_data['main']['humidity']),
            "main": str(list_of_data['weather'][0]['main']),
            "description": str(list_of_data['weather'][0]['description']),
            "icon": list_of_data['weather'][0]['icon'],
            "name": str(list_of_data['name']),
            "wind": str(list_of_data['wind']['speed'])
        }
        print(data)

    else:
        data = {}
    
    return render(request, 'index.html', {"data": data})


