from django.contrib import admin
from django.http import HttpRequest
from django.urls import reverse
from django.utils.html import format_html
from urllib.parse import urlencode
from django.db.models import Count
from . import models
# Register our models for admin interface

# Register user model to admin site
@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):

    # display custom fields in admin interface
    list_display = ["username", "first_name", "last_name", "email", "address", "phone_number", "families_count"]

    # create a custom method that generate a link to user's family
    def families_count(self, family: models.User):
        url = (
            reverse("admin:communityhub_family_changelist")
                + "?"
                + urlencode({
                "family__id": str(family.id)
                })
            )
        return format_html("<a href='{}'>{}</a>", url, family.families_count)

    # Overrides the default queryset to annotate each user instance with the count of associated families.
    def get_queryset(self, request: HttpRequest):
        return super().get_queryset(request).annotate(
            families_count = Count("family")
        )



# Register family model to admin site
@admin.register(models.Family)
class FamilyAdmin(admin.ModelAdmin):

    # display custom fields in admin interface
    list_display = ["first_name", "last_name", "father_name", "family_relationship", "get_user"]

    # create a custom method that generate a link to the user of each family
    def get_user(self, obj: models.Family):
        url = (
            reverse("admin:communityhub_user_changelist")
                + "?"
                + urlencode({
                "user__id": str(obj.user.id)
                })
            )
        return format_html('<a href="{}">{}</a>', url, obj.user.username)

    # define a column name for related object
    get_user.short_description = "User"

# Register group model to admin site
@admin.register(models.Group)
class GroupAdminO(admin.ModelAdmin):

    # display custom fields in admin interface
    list_display = ["title", "description"]


# Register event model in admin site
@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):

    # display custom fields in admin interface
    list_display = ["title", "description", "event_type", "event_date", "event_time", "image", "get_group"]

    # create a custom method that generate a link to the responsable group of the event
    # if an event is private and needs a group to be responsable, it will generate a link to responsable group
    def get_group(self, obj: models.Event):
        if obj.group:
            url = reverse("admin:communityhub_group_change", args=[obj.group.id])
            return format_html('<a href="{}">{}</a>', url, obj.group.title)
        return "No Group"

    # define a column name for related object
    get_group.short_description = "Responsable Group"


# Resigter event participant model in admin site
@admin.register(models.EventParticipant)
class EventParticipantAdmin(admin.ModelAdmin):

    # display custom fields in admin interface
    list_display = ["event", "user"]


# Register group participant model in admin site
@admin.register(models.GroupParticipant)
class GroupParticipantAdmin(admin.ModelAdmin):

    # display custom fields in admin interface
    list_display = ["participant_type", "get_group", "user"]

    # Define a custom method to display groups as clickable links
    def get_group(self, obj: models.GroupParticipant):
        groups = obj.group.all()
        links = []
        for group in groups:
            url = reverse("admin:communityhub_group_change", args=[group.id])
            return format_html('<a href="{}">{}</a>', url, group.title)
        return " | ".join(links)

    # define a column name for related object
    get_group.short_description = "Group Joined"