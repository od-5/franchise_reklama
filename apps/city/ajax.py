# coding: utf-8
from annoying.decorators import ajax_request
from .models import City

__author__ = 'alexy'


@ajax_request
def city_map(request):
    request.encoding = 'utf-8'
    if request.is_ajax():
        query = City.objects.all()
        result = []
        for item in query:
            result_json = {}
            result_json['name'] = item.name
            result_json['coord_x'] = float(item.coord_x)
            result_json['coord_y'] = float(item.coord_y)
            result.append(result_json)
        data = result
    else:
        data = {'error': True}
    return data
