from django.urls import path, include
#라우터 기반으로 작성
from rest_framework.routers import DefaultRouter
from track_module import views
from rest_framework import renderers

#라우터 기준으로 객체 생성
#router = DefaultRouter()
#router.register(r'SendRecieveInfo', views.SendRecieveViewSet)#delivery이름의 viewset
#router.register(r'DeliveryMan', views.DeliveryManViewSet)
"""
urlpatterns = [
    #path('', include(router.urls)),
]
"""

urlpatterns = [
    #path('', track_module.views.home, name="home"),
    #path('userselect/', track_module.views.userSelect, name="userselct"),
    #path('search/', track_module.views.Search, name="search"),
    path('', views.SendRecieveView.as_view(), name="list"), #첫화면

    #user select
    path('userselect/', views.SendRecieveSelectView.as_view(), name="userselect"),
    
    #user search
    path('search/', views.SendRecieveSearchView.as_view(), name="search"),
    
    path("create/", views.SendRecieveCreate.as_view(), name="create"), #택배 생성
    path("read/<int:pk>", views.SendRecieveRead.as_view(), name="read"),#택배 위치 검색
    path("deliveryMan/list/", views.DeliveryManView.as_view(), name="DM_list"),
    path("deliveryMan/create/", views.DeliveryManCreate.as_view(), name="DM_create"),
    path("deliveryMan/read/<int:pk>", views.DeliveryManRead.as_view(), name="DM_read"),
    path("deliveryMan/update/<int:pk>", views.DeliveryManUpdate.as_view(), name="DM_update"),
]