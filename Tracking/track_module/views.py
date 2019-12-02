"""
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import SendRecieveInfo, DeliveryMan
from .serializers import SendRecieveSerializer, DeliveryManSerializer
from rest_framework.filters import SearchFilter
from rest_framework.response import Response



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
"""

from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import SendRecieveInfo, DeliveryMan

class SendRecieveView(ListView):
    template_name = 'SendRecieveInfoCRUD/list.html'
    context_object_name = 'send_recieve'
    model = SendRecieveInfo

class SendRecieveCreate(CreateView):
    template_name = 'SendRecieveInfoCRUD/form.html'
    model = SendRecieveInfo
    fields = ["Sender_Name", "Sender_phone", "Sender_addr", 
        "Reciever_Name", "Reciever_phone", "Reciever_addr"]
    success_url = reverse_lazy("list")

class SendRecieveRead(DetailView):
    template_name = 'SendRecieveInfoCRUD/detail.html'
    context_object_name = 'send_recieve'
    model = SendRecieveInfo