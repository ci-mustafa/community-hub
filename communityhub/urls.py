from django.urls import path, include
from . import views

urlpatterns = [
    path('event/<int:pk>/', views.event_detail, name='event_detail'),
]