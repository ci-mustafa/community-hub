"""
URL configuration for community project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import debug_toolbar

# Set admin site header
admin.site.site_header = "Community Hub Administration"
# Set admin area title
admin.site.index_title = "Admin Dashboard"
urlpatterns = [
    path('admin/', admin.site.urls),
    path("__debug__", include(debug_toolbar.urls)),

    # Registration and authentication urls
    path("communityhub/auth/", include("djoser.urls")),
    path("communityhub/auth/", include("djoser.urls.jwt")),
    path("communityhub/", include("communityhub.urls"))
]
