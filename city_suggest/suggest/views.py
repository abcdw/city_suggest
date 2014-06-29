from django.shortcuts import render
from django.http import HttpResponse

import json
from cities_light.models import City
# Create your views here.

def index(request):
    return render(request, 'suggest/index.html')

def get_cities(request):
    if True: #request.is_ajax():
        query = request.GET.get('filter', '')
        cities = City.objects.filter(name__icontains = query )[:20]
        result = []
        for city in cities:
            city_json = {}
            city_json['name'] = city.name
            city_json['country'] = city.country.name
            result.append(city_json)
        data = json.dumps(result)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

