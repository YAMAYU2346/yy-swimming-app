from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Match
from .serializers import MatchSerializer
import uuid

@api_view()
def match_list(request):
    return Response({"matchList": Match.objects.all()})


# @api_view(['GET', 'POST'])
# def matches(request):
#     if request.method == 'GET':
#         print(request.query_params["id"])
#         match = {
#             'id': '1',
#             'name': 'ISL 2022',
#             'numOfTeams': 4,
#             'entryURL': '',
#             'data': ''
#         }
#     elif request.method == 'POST':
#         # match = request.data
#         match['id'] = uuid.uuid1()
#         Match.objects.create(match)
#         return Response(match)
#     elif request.method == 'PUT':
#         # match = request.data
#         match = {
#             'id': '1',
#             'name': 'ISL 2022',
#             'numOfTeams': 4,
#             'entryURL': '',
#             'data': ''
#         }
#         return Response(match)

class MatchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    # permission_classes = [permissions.IsAuthenticated]
