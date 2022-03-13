from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


def home(request):
    return render(request, 'index.html')


# Create your views here.
@api_view(['GET', 'POST'])
def firstAPI(request):
    if request.method == 'POST':
        name = request.data['name']
        age = request.data['age']
        return Response({'name': name, 'age': age})
    else:
        context = {
            'name': 'Default Name',
            'age': 500
        }
    return Response(context)
