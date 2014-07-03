from django.shortcuts import render
from django.http import HttpResponse

import json
from cities_light.models import City
# Create your views here.


def index(request):
    return render(request, 'suggest/index.html')


def get_cities(request):
    data = 'fail'
    if request.is_ajax():
        query = request.GET.get('filter', '').split(', ')
        if len(query) > 1:
            cities = City.objects.filter(name__icontains=query[0],
                                         country__name__icontains=query[1]
                                         )[:20]
        else:
            cities = City.objects.filter(name__icontains=query[0])[:20]
        result = []
        for city in cities:
            city_json = {}
            city_json['name'] = city.name
            city_json['country'] = city.country.name
            result.append(city_json)
        data = json.dumps(result)

    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def get_city_info(request):
    data = 'fail'
    if request.is_ajax():
        query = request.GET.get('filter', '').split(', ')
        if len(query) > 1:
            city = City.objects.get(name=query[0],
                                    country__name=query[1])
            city_json = {}
            city_json['region'] = city.region.name
            city_json['population'] = city.population
            city_json['feature_code'] = city.feature_code
            city_json['coords'] = str(city.latitude) + ", " \
                                + str(city.longitude)
            data = json.dumps(city_json)

    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
