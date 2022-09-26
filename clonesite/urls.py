from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from common.models import User
from rest_framework import routers, serializers, viewsets

# Wire up our API using automatic URL routing
# Additionally, we include login URLs for the browable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('boltnnut/', include('boltnnut.urls')),
    path('common/', include('common.urls')),
    path('api/', include('api.urls')),
    path('api_auth/', include('rest_framework.urls', namespace='rest_framework')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
