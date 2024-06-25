from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreateSerializer # type: ignore
from rest_framework.serializers import ModelSerializer # type: ignore
from rest_framework import serializers # type: ignore
from . import models

# Create events serializer
class EventSerializer(ModelSerializer):
    class Meta:
        model = models.Event
        fields = [
            "title", "description", "image",
            "event_type", "event_date", "event_time",
            "location_name", "group"
        ]

# Create event participants serializer
class EventParticipantsSerializer(ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = models.EventParticipant
        fields = ["user"]

    def create(self, validated_data):
        event_id = self.context["event_id"]
        user_id = self.context["user_id"]
        return models.EventParticipant.objects.create(
            event_id= event_id, user_id = user_id, **validated_data
            )

# Create groups serializer
class GroupSerializer(ModelSerializer):
    class Meta:
        model = models.Group
        fields = ["title", "description"]

# create group participant serialzier
class GroupParticipantSerializer(ModelSerializer):
    class Meta:
        model = models.GroupParticipant
        fields = ["participant_type", "user", "group"]

# create family serialzier
class FamilySerializer(ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = models.Family
        fields = ["first_name", "last_name", "father_name", "family_relationship", "user"]

    def create(self, validated_data):
        user_id = self.context["user_id"]
        return models.Family.objects.create(
            user_id = user_id, **validated_data
            )

# Registration endpoint
# Define a custom UserCreateSerializer that extends BaseUserCreateSerializer
class UserCreateSerializer(BaseUserCreateSerializer):
    # Meta class to extend or modify behavior of BaseUserCreateSerializer.Meta
    class Meta(BaseUserCreateSerializer.Meta):
        # Specify the fields that should be included in the serializer
        fields = ["username", "email", "first_name", "last_name", "password"]

# Current user endpoint
# Define a custom UserSerializer that extends BaseUserSerializer
class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        # Specify the fields that should be included in the serializer
        fields = [
            'profile_image', 'username', "email", "first_name",
            "last_name", "father_full_name", "grand_father_full_name",
            "birth_date", "place_of_birth", "country", "province", "village",
            "district", "marital_status", "country_of_residence", "occupation",
            "address", "phone_number", "gender", "has_children", "underage_children_count",
            "total_children",
        ]




