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
from rest_framework.filters import SearchFilter

class SendRecieveView(ListView):
    template_name = 'select.html'
    context_object_name = 'send_recieve'
    model = SendRecieveInfo

class SendRecieveSelectView(ListView):
    template_name = 'userselect.html'
    model = DeliveryMan
    
class SendRecieveCreate(CreateView):
    template_name = 'SendRecieveInfoCRUD/form.html'
    model = SendRecieveInfo
    fields = ["Sender_Name", "Sender_phone", "Sender_addr", 
        "Reciever_Name", "Reciever_phone", "Reciever_addr"]
    success_url = reverse_lazy("list")
    #택배 등록될때 자동으로 db하나 저장되게 만들어야함

class SendRecieveSearchView(ListView):
    template_name = 'search.html'
    model = DeliveryMan
    context_object_name = 'deliveryMan'

    def get_queryset(self):
        qs = super().get_queryset()
        q = str(self.request.GET.get('ParcelNums', ''))
        if q:
            #print(q)
            #print(type(qs.filter(ParcelNums__ParcelNum = q)))
            deliveryMan_list = qs.filter(ParcelNums__ParcelNum__contains = q)
            deliveryMan = deliveryMan_list.values()
            #print(deliveryMan)
            return deliveryMan
        else:
            return None

            
class SendRecieveRead(DetailView):
    template_name = 'SendRecieveInfoCRUD/detail.html'
    context_object_name = 'send_recieve'
    model = SendRecieveInfo

class DeliveryManView(ListView):
    template_name = 'DeliveryMan/DM_list.html'
    context_object_name = 'deliveryMan'
    model = DeliveryMan

class DeliveryManCreate(CreateView):
    template_name = 'DeliveryMan/DM_form.html'
    model = DeliveryMan
    fields = ["DeliveryMan_Name", "ManPhone", "ParcelNums", 
            "ParcelLocation", "ParcelStatus"]
    success_url = reverse_lazy("list")

class DeliveryManRead(DetailView): #택배번호로 디테일 보여주기로 함수 바꾸기
    template_name = 'DeliveryMan/DM_detail.html'
    context_object_name = 'deliveryMan'
    model = DeliveryMan

class DeliveryManUpdate(UpdateView):
    template_name = 'DeliveryMan/DM_form.html'
    model = DeliveryMan
    fields = ["DeliveryMan_Name", "ManPhone", "ParcelNums", 
            "ParcelLocation", "ParcelStatus"]
    success_url = reverse_lazy("list")

'''
def home(request):
    return render(request, 'select.html')

def userSelect(request):
    return render(request, 'userselect.html')

def Search(request):
    qs = DeliveryMan.objects.all()
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(ParcelNums__icontains = q)
    return render(request, 'search.html', 
        {'DeliveryMan_list' : qs,
        'q' : q})

'''
