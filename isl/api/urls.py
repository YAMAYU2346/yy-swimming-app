from django.urls import include, path
from rest_framework import routers
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from . import apis
from . import api_views

router = routers.DefaultRouter()
# router.register(r'matches', api_views.MatchViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    # path('api/', apis.api.as_view(), name = "api"),
    # path('api/matches/list',api_views.match_list),
    # path('api/matches/',api_views.matches),
]