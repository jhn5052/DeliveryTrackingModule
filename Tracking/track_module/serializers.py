from .models import Sender, Reciever, Parcel, DeliveryMan
from rest_framework import serializers

class SenderSerializer(serializers.ModelSerializer):
    class Meta:
        #어떤 모델을 serializer시킬건지
        model = Sender
        fields = '__all__'

class RecieverSerializer(serializers.ModelSerializer):
    class Meta:
        #어떤 모델을 serializer시킬건지
        model = Reciever
        fields = '__all__'

class ParcelSerializer(serializers.ModelSerializer):
    class Meta:
        #어떤 모델을 serializer시킬건지
        model = Parcel
        fields = '__all__'

class DeliveryManSerializer(serializers.ModelSerializer):
    class Meta:
        #어떤 모델을 serializer시킬건지
        model = DeliveryMan
        fields = '__all__'