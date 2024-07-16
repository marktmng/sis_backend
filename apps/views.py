from rest_framework import viewsets 
from django.shortcuts import render
from .serializers import RegistrationSerializer
from .models import Registration

# Create your views here.

class RegistrationView(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
