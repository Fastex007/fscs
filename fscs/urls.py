from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('home.urls')),
    path('auth/', include('users.urls')),
    path('admin/', admin.site.urls),
    path('references/', include('references.urls')),
    path('flights/', include('flights.urls')),

    path(r'^api/', include('rest_framework.urls', namespace='rest_framework'))
]
