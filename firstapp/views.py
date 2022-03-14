from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User


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


# Registration

@api_view(['POST'])
def registrstionAPI(request):
    if request.method == 'POST':
        username = request.data['username']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        password1 = request.data['password1']
        password2 = request.data['password2']
        email = request.data['email']

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username is already exists'})
        if password1 != password2:
            return Response({'error': 'Password did not match '})
        else:
            user = User()
            user.username = username
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.is_active = True
            user.is_staff = True
            user.set_password(raw_password=password1)
            user.save()
            return Response({'success': 'User is created successfully'})
