from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from . import models
# Register our models for admin interface

# Register user model to admin site
@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):

    # display custom fields in admin interface
    list_display = ["username", "first_name", "last_name", "email", "address", "phone_number", "get_family"]

    # create a custom method that generate a link to each family member
    def get_family(self, obj: models.User):
        links = []
        for family in obj.family.all():
            url = reverse("admin:communityhub_family_change", args=[family.id])
            links.append(format_html('<a href="{}">{}</a>', url, family.first_name))
        return format_html("  |  ".join(links))

    # define a column name for related object
    get_family.short_description = "Family Member"


# Register family model to admin site
@admin.register(models.Family)
class FamilyAdmin(admin.ModelAdmin):

    # display custom fields in admin interface
    list_display = ["first_name", "last_name", "father_name", "family_relationship", "get_user"]

    # create a custom method that generate a link to the user of each family
    def get_user(self, obj: models.Family):
        url = reverse("admin:communityhub_user_change", args=[obj.user.id])
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
    list_display = ["event", "user"]


# Register group participant model in admin site
@admin.register(models.GroupParticipant)
class GroupParticipantAdmin(admin.ModelAdmin):
    list_display = ["participant_type", "group", "user"]