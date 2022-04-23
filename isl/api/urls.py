from django.urls import path
from . import apis
from . import api_views

urlpatterns = [
    path('api/', apis.api.as_view(), name = "api"),
    path('api/events/list',api_views.event_list),
]