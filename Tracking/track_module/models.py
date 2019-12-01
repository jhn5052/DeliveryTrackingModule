from django.db import models
from django.conf import settings

class SendRecieveInfo(models.Model):
    Sender_Name = models.CharField(max_length=100, default="null")
    Sender_phone = models.CharField(max_length=100, default="null")
    Sender_addr = models.CharField(max_length=100, default="null")
    Sender_date = models.DateField(auto_now = True)
    Reciever_Name = models.CharField(max_length=100, default="null")
    Reciever_phone = models.CharField(max_length=100, default="null")
    Reciever_addr = models.CharField(max_length=100, default="null")

    def number():
        no = SendRecieveInfo.objects.count()
        if no == 0:
            return 150000000
        else:
            return no + 150000000


    ParcelNum = models.IntegerField(default=number, unique=True, primary_key=True)
    def __str__(self):
        return str(self.ParcelNum)


class DeliveryMan(models.Model):
    DeliveryMan_Name = models.CharField(max_length=50, default="홍길동")
    ManPhone = models.CharField(max_length=50, default="null")
    #ParcelNum = models.ForeignKey(
    #    SendRecieveInfo, 
    #    on_delete=models.CASCADE,
    #    related_name='SendRecieveInfo',
    #    null=True
    #)
    ParcelNum = models.ManyToManyField(SendRecieveInfo)
    Update_date = models.DateField(auto_now = True)
    ParcelLocation = models.CharField(max_length=100, default="한국외대")
    ParcelStatus = models.CharField(max_length=100, default="배송 준비중")

    def __str__(self):
        return self.ParcelNum