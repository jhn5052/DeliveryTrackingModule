from django.contrib import admin
from django.urls import path, include
from track_module import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('track_module.urls')),
]
