from django.shortcuts import render
from rest_framework import viewsets
from .models import Sender, Reciever, Parcel, DeliveryMan
from .serializers import SenderSerializer, RecieverSerializer, ParcelSerializer, DeliveryManSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Sender.objects.all()
    serializer_class = SenderSerializer #Serializer class초기화