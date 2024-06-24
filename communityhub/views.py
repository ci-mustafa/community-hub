from django.shortcuts import get_object_or_404
from geopy.geocoders import Nominatim # type: ignore
from rest_framework.viewsets import ModelViewSet  # type: ignore
from rest_framework.decorators import action # type: ignore
from rest_framework.response import Response # type: ignore
from . import serializers
from . import models


class EventViewSet(ModelViewSet):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer

    def retrieve(self, request, pk=None):
        # Retrieve the Event object based on the provided primary key (pk)
        event = get_object_or_404(models.Event, pk=pk)

        # Extract the location name from the Event object
        location_name = event.location_name

        # Initialize latitude and longitude to None
        latitude, longitude = None, None

        # Check if location_name is provided
        if location_name:
            # Initialize a Geopy geolocator
            geolocator = Nominatim(user_agent="communityhub")

            # Attempt to geocode the location name to retrieve coordinates
            location = geolocator.geocode(location_name)

            # If location is found, extract latitude and longitude
            if location:
                latitude, longitude = location.latitude, location.longitude

        # Prepare the data dictionary with location_name, latitude, and longitude
        data = {
            'location_name': location_name,
            'latitude': latitude,
            'longitude': longitude
        }

        # Combine event data with location data
        event_data = serializers.EventSerializer(event).data
        event_data.update(data)

        # Return the combined data as a JSON response
        return Response(event_data)
