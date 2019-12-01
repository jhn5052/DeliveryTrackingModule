from django.contrib import admin
from django.urls import path, include, re_path
from track_module import urls
from rest_framework import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('track_module.urls')),
    path('api-auth/', include('rest_framework.urls')), #login
]
