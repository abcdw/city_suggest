from django.shortcuts import render
from django.http import HttpResponse

import json
from cities_light.models import City
# Create your views here.

def index(request):
    return render(request, 'suggest/index.html')

def get_cities(request):
    if True: #request.is_ajax():
        q = request.GET.get('filter', '')
        cities = City.objects.filter(name__icontains = q )[:20]
        results = []
        for city in cities:
            city_json = {}
            city_json['id'] = city.name
            results.append(city_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

