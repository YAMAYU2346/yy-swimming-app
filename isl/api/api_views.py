from rest_framework.decorators import api_view
from rest_framework.response import Response
# from .models import Customer


@api_view()
def event_list(request):
    print(request)
    event_list = [{
        'id': '1',
        'name': 'ISL 2022',
        'numOfTeams': 4,
        'entryURL': ''
    }]
    return Response({"eventList": event_list})


@api_view(['GET', 'POST'])
def events(request):
    if request.method == 'GET':
        '''HTTP GET'''
    elif request.method == 'POST':
        '''HTTP POST'''
    event_list = [{
        'id': '1',
        'name': 'ISL 2022',
        'numOfTeams': 4,
        'entryURL': ''
    }]
    return Response({"eventList": event_list})
