from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer # type: ignore


# Define a custom UserCreateSerializer that extends BaseUserCreateSerializer
class UserCreateSerializer(BaseUserCreateSerializer):
    # Meta class to extend or modify behavior of BaseUserCreateSerializer.Meta
    class Meta(BaseUserCreateSerializer.Meta):
        # Specify the fields that should be included in the serializer
        fields = ["username", "email", "first_name", "last_name", "password"]



