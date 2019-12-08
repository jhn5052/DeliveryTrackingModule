from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import SendRecieveInfo, DeliveryMan
from rest_framework.filters import SearchFilter


#메인 페이지 렌더링
class SendRecieveView(ListView):
    template_name = 'select.html'
    context_object_name = 'send_recieve'
    model = SendRecieveInfo

#클라이언트 화면 페이지 렌더링
class SendRecieveSelectView(ListView):
    template_name = 'userselect.html'
    model = DeliveryMan
    
#발송인-수신인(택배 등록) 새로운 DB 생성
class SendRecieveCreate(CreateView):
    template_name= 'SendRecieveInfoCRUD/form.html'
    model = SendRecieveInfo
    fields = ["Sender_Name", "Sender_phone", "Sender_addr", 
        "Reciever_Name", "Reciever_phone", "Reciever_addr"]

    #택배가 새로 등록되면 기본적으로 택배 상태 DB 저장
    def get_success_url(self):
        qs = SendRecieveInfo.objects.get(ParcelNum = self.object.ParcelNum)
        new_Parcel = DeliveryMan(DeliveryMan_Name="미정", ManPhone="미정", ParcelNums = qs,ParcelLocation="한국외대" ,ParcelStatus="배송준비중")
        new_Parcel.save(force_insert=True)
        return reverse_lazy('read', kwargs={'pk' : self.object.ParcelNum})
    
#택배 운송장 번호로 DB검색
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
            deliveryMan_list = qs.filter(ParcelNums__ParcelNum = q)
            deliveryMan = deliveryMan_list.values()
            print(deliveryMan)
            return deliveryMan
        else:
            return None

#택배(발송인, 수신인) 상세 정보 페이지
class SendRecieveRead(DetailView):
    template_name = 'SendRecieveInfoCRUD/detail.html'
    context_object_name = 'send_recieve'
    model = SendRecieveInfo

#택배기사 layer : 배송중인 택배 상태 DB list
class DeliveryManView(ListView):
    template_name = 'DeliveryMan/DM_list.html'
    context_object_name = 'deliveryMan'
    model = DeliveryMan

#택배 상태 업데이트
class DeliveryManCreate(CreateView):
    template_name = 'DeliveryMan/DM_form.html'
    model = DeliveryMan
    fields = ["DeliveryMan_Name", "ManPhone", "ParcelNums", 
            "ParcelLocation", "ParcelStatus"]
    success_url = reverse_lazy("list")

#택배(택배 기사 layer) 상세 정보
class DeliveryManRead(DetailView):
    template_name = 'DeliveryMan/DM_detail.html'
    context_object_name = 'deliveryMan'
    model = DeliveryMan

