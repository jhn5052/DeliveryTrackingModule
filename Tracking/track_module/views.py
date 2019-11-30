from django.shortcuts import render
from rest_framework import viewsets
from .models import SendRecieveInfo, Parcel, DeliveryMan
from .serializers import SendRecieveSerializer, ParcelSerializer, DeliveryManSerializer
from rest_framework.filters import SearchFilter

class SendRecieveViewSet(viewsets.ModelViewSet):
    queryset = SendRecieveInfo.objects.all()
    serializer_class = SendRecieveSerializer

    filter_backends = [SearchFilter]
    search_fields = ('Sender_Name', 'Reciever_Name', 'ParcelNum')
    
    def get_queryset(self):
        qs = super().get_queryset()
        return qs

class ParcelViewSet(viewsets.ModelViewSet):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer
    filter_backends = [SearchFilter]
    search_fields = ('SendRecieveInfo__ParcelNum',)#FK search solution not yet

    def get_queryset(self):
        qs = super().get_queryset()
        return qs

class DeliveryManViewSet(viewsets.ModelViewSet):
    queryset = DeliveryMan.objects.all()
    serializer_class = DeliveryManSerializer

    filter_backends = [SearchFilter]
    search_fields = ('author','SendRecieveInfo__ParcelNum')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated:
            qs = qs.filter(author=self.request.user)
        else:
            qs = qs.none()
            return exit(-1) #sever error
        return qs
        
    