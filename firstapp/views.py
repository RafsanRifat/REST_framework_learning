from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET', 'POST'])
def firstAPI(request):
    if request.method == 'POST':
        name = request.data['name']
        age = request.data['age']
        return Response({'name': name, 'age': age})
    context = {
        'name': 'Testname',
        'Varsity': 'TestVarsity'
    }
    return Response(context)
