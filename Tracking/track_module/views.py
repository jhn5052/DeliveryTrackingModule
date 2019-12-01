from django.shortcuts import render
from rest_framework import viewsets
from .models import SendRecieveInfo, DeliveryMan
from .serializers import SendRecieveSerializer, DeliveryManSerializer
from rest_framework.filters import SearchFilter

class SendRecieveViewSet(viewsets.ModelViewSet):
    queryset = SendRecieveInfo.objects.all()
    serializer_class = SendRecieveSerializer

    filter_backends = [SearchFilter]
    search_fields = ('Sender_Name', 'Reciever_Name', 'ParcelNum')
    
    def get_queryset(self):
        qs = super().get_queryset()
        return qs


class DeliveryManViewSet(viewsets.ModelViewSet):
    queryset = DeliveryMan.objects.all()
    serializer_class = DeliveryManSerializer

    filter_backends = [SearchFilter]
    search_fields = ('ParcelNums__ParcelNum',)

    def get_queryset(self):
        qs = super().get_queryset()
        #if self.request.user.is_authenticated: #관리자
        #    qs = super().get_queryset()
        #    qs = qs.filter(author=self.request.user)
        #else: #아닐때
        #    return qs 
        return qs
        
