from django.urls import path
from .views import firstAPI, registrstionAPI

urlpatterns = [
    path('first/', firstAPI, name="api"),
    path('registration/', registrstionAPI, name="registration"),
]
