from django.shortcuts import get_object_or_404
from geopy.geocoders import Nominatim # type: ignore
from rest_framework.viewsets import ModelViewSet  # type: ignore
from rest_framework.decorators import action # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework.permissions import IsAuthenticated, IsAdminUser # type: ignore
from rest_framework import status # type: ignore
from . import serializers
from . import models


# Create events endpoints
class EventViewSet(ModelViewSet):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer

    # Applying permissions
    def get_permissions(self):
        if self.request.method == "GET":
            return [IsAuthenticated()]
        return [IsAdminUser()]
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


# Create event participant endpoints
class EventParticipantsViewSet(ModelViewSet):
    serializer_class = serializers.EventParticipantsSerializer

    # Applying permissions
    def get_permissions(self):
        if self.request.method in ["GET", "POST"]:
            return [IsAuthenticated()]
        return [IsAdminUser()]

    def get_queryset(self):
        event_id = self.kwargs.get('event_pk')
        return models.EventParticipant.objects.filter(event_id=event_id)

    def create(self, request, **kwargs):
        event_id = self.kwargs.get('event_pk')
        user_id = request.user.id
        serializer_context = {
            'event_id': event_id,
            'user_id': user_id,
        }
        serializer = self.get_serializer(data=request.data, context=serializer_context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# Create group endpoint
class GroupViewSet(ModelViewSet):
    queryset = models.Group.objects.all()
    serializer_class = serializers.GroupSerializer


# create group participant endpoint
class GroupParticipantVeiwSet(ModelViewSet):
    queryset = models.GroupParticipant.objects.all()
    serializer_class = serializers.GroupParticipantSerializer


# create family endpoint
class FamilyViewSet(ModelViewSet):
    serializer_class = serializers.FamilySerializer

    def get_queryset(self):
        user_id = self.request.user.id
        return models.Family.objects.filter(user_id=user_id)

    def create(self, request):
        user_id = request.user.id
        serializer_context = {
            'user_id': user_id,
        }
        serializer = self.get_serializer(data=request.data, context=serializer_context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


