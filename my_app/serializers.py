from rest_framework import serializers
from .models import Company,Contact

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta :
        model = Company
        fields = '__all__'

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
