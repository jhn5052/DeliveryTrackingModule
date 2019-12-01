from django.urls import path, include
#라우터 기반으로 작성
from rest_framework.routers import DefaultRouter
from track_module import views

#라우터 기준으로 객체 생성
router = DefaultRouter()
router.register(r'SendRecieveInfo', views.SendRecieveViewSet)#delivery이름의 viewset
router.register(r'DeliveryMan', views.DeliveryManViewSet)
urlpatterns = [
    path('', include(router.urls)),
]