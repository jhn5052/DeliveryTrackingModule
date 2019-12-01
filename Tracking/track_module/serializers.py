from .models import SendRecieveInfo, DeliveryMan
from rest_framework import serializers

class SendRecieveSerializer(serializers.ModelSerializer):
    Parcel_Num = serializers.ReadOnlyField(source="ParcelNum")
    class Meta:
        model = SendRecieveInfo
        fields = ('Sender_Name', 'Sender_phone', 'Sender_addr', 'Sender_date',
                'Reciever_Name', 'Reciever_phone', 'Reciever_addr', 'Parcel_Num')
        #fields = '__all__'

class DeliveryManSerializer(serializers.ModelSerializer):
    class Meta:
        #어떤 모델을 serializer시킬건지
        model = DeliveryMan
        fields = ('DeliveryMan_Name', 'ManPhone', 'ParcelNums', 'Update_date', 'ParcelLocation','ParcelStatus')
