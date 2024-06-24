from django.urls import path, include
from rest_framework.routers import SimpleRouter # type: ignore
from . import views

router = SimpleRouter()
router.register("events", views.EventViewSet)
urlpatterns = [
    path("", include(router.urls))
]