from django.urls import path
from .views import firstAPI, registrstionAPI, ContactAPIView

urlpatterns = [
    path('first/', firstAPI, name="api"),
    path('contact/', ContactAPIView.as_view(), name="contact"),
    path('registration/', registrstionAPI, name="registration"),
]
