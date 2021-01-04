from django.shortcuts import render
import requests
from django.views.generic.base import TemplateView
from .models import City
from .forms import CityForm
 
def index(request):
    api_key = '47407e96c591bb5491f2f43cbfa49693'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid='+api_key

    if (request.method == 'POST'):
        form = CityForm(request.POST)
        form.save() # созраняем данные в бд

    form = CityForm()

    cities = City.objects.all()
    all_cities = []

    for city in cities:
        print(city)
        response  = requests.get(url.format(city)).json()
        city_info = {
            'city': city.name,
            'temp': response["main"]["temp"],
            'icon': response["weather"][-1]["icon"]
        }
        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}

    return render(request, 'index.html', context)
