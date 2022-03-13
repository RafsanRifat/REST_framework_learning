from django.urls import path
from .views import firstAPI

urlpatterns = [
    path('first/', firstAPI, name="api"),
]
