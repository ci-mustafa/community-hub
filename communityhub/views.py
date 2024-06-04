from django.shortcuts import render
from .models import Event
from geopy.geocoders import Nominatim # type: ignore

def event_detail(request, pk):
    # Retrieve the Event object based on the provided primary key (pk)
    event = Event.objects.get(pk=pk)

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


    # Prepare the context dictionary with location_name, latitude, and longitude
    context = {
        'location_name': location_name,
        'latitude': latitude,
        'longitude': longitude
    }

    # Render the event_detail.html template with the context data
    return render(request, 'event_detail.html', context)
