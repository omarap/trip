from .models import Client, Destination
from rest_framework import serializers 

# Serializers define the API representation.
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['name','latitude', 'longitude']

# Serializers define the API representation.
class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = ['name','latitude', 'longitude','date']