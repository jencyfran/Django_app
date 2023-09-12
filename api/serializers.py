from rest_framework import serializers
from .models import Location, Item

# Serializer for the Item model

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('__all__')


# Serializer for the Location model

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('__all__')

