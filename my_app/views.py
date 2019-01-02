from django.shortcuts import render
from rest_framework import viewsets
from .models import Company,Contact
from .serializers import CompanySerializer,ContactSerializer

class CompanyView(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class ContactView(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
