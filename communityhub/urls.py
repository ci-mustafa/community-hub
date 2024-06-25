from django.urls import path, include
from rest_framework_nested import routers # type: ignore
from . import views

router = routers.DefaultRouter()
router.register("events", views.EventViewSet)
router.register("groups", views.GroupViewSet)
events_router = routers.NestedDefaultRouter(router, "events", lookup="event")
events_router.register("participants", views.EventParticipantsViewSet, basename="event-participants")
urlpatterns = [
    path("", include(router.urls)),
    path("", include(events_router.urls)),
]