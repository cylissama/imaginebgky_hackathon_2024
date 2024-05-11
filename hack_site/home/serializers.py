from rest_framework import serializers
from .models import PointOfInterest,Route

class PointOfInterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointOfInterest
        fields = '__all__'

class RouteSerializer(serializers.ModelSerializer):
    points = PointOfInterestSerializer(many=True, read_only=True)

    class Meta:
        model = Route
        fields = '__all__'