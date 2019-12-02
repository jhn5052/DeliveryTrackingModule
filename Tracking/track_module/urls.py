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
    path("", views.SendRecieveView.as_view(), name="list"), #전체 DB list보여줌
    path("create/", views.SendRecieveCreate.as_view(), name="create"), #택배 생성
    path("read/<int:pk>", views.SendRecieveRead.as_view(), name="read"),#택배 위치 검색
    #path("deliveryMan/create/", views.DeliveryManCreate.as_view(), name="")
    #path("delete/<int:pk>", views.)
]