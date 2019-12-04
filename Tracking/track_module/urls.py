from django.urls import path, include
from rest_framework.routers import DefaultRouter
from track_module import views
from rest_framework import renderers


urlpatterns = [
    #첫화면
    path('', views.SendRecieveView.as_view(), name="list"), 

    #user select
    path('userselect/', views.SendRecieveSelectView.as_view(), name="userselect"),
    
    #user search
    path('search/', views.SendRecieveSearchView.as_view(), name="search"),
    path("create/", views.SendRecieveCreate.as_view(), name="create"), #택배 생성
    path("read/<int:pk>", views.SendRecieveRead.as_view(), name="read"),#택배 위치 검색
    path("deliveryMan/list/", views.DeliveryManView.as_view(), name="DM_list"),
    path("deliveryMan/create/", views.DeliveryManCreate.as_view(), name="DM_create"),
    path("deliveryMan/read/<int:pk>", views.DeliveryManRead.as_view(), name="DM_read"),
]
