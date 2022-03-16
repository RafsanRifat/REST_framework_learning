from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Contact
from rest_framework.views import APIView


def home(request):
    return render(request, 'index.html')


# Create your views here.
@api_view(['GET', 'POST'])
# @permission_classes([AllowAny])
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


# @permission_classes([AllowAny])
class ContactAPIView(APIView):
    def post(self, request, format=None):
        data = request.data
        email = request.data['email']
        name = request.data['name']
        phone = request.data['phone']
        subject = request.data['subject']
        details = request.data['details']

        contact = Contact(name=name, email=email, phone=phone, subject=subject, details=details)

        contact.save()
        return Response({'success': 'successfully saved your data'})

    def get(self, request, format=None):
        return Response({'message:': 'get request working'})
