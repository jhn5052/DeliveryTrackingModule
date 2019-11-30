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
    #auto_increment_id = models.AutoField(primary_key=True)

    def number():
        no = SendRecieveInfo.objects.count()
        if no == 0:
            return 150000000
        else:
            return no + 150000000


    ParcelNum = models.IntegerField(default=number, unique=True, primary_key=True)
    

    def __str__(self):
        return str(self.ParcelNum)

class Parcel(models.Model):
    ParcelUpdate = models.BooleanField(default=True) #택배 상태 update될 때
    ParcelStatus = models.CharField(max_length=100, default="배송 준비중")
    ParcelNum = models.ForeignKey(
        SendRecieveInfo,
        on_delete=models.CASCADE,
        null=True
    )
    def __str__(self):
        return str(self.ParcelNum)

class DeliveryMan(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        default=1,
        on_delete=models.CASCADE
    )
    ManPhone = models.CharField(max_length=50, default="null") #별로 필요 없을 듯
    ParcelNum = models.ForeignKey(
        SendRecieveInfo, 
        on_delete=models.CASCADE,
        null=True
    )
    def __str__(self):
        return self.author