from django.db import models
from django.conf import settings
from django.utils import timezone

#클라이언트가 택배 등록(모델 : 발송인, 수신인관한 정보 저장)
class SendRecieveInfo(models.Model):
    Sender_Name = models.CharField(max_length=100, default='')
    Sender_phone = models.CharField(max_length=100, default='')
    Sender_addr = models.CharField(max_length=100, default='')
    Sender_date = models.DateTimeField(auto_now_add = True)
    Reciever_Name = models.CharField(max_length=100, default='')
    Reciever_phone = models.CharField(max_length=100, default='')
    Reciever_addr = models.CharField(max_length=100, default='')

    #운송장 번호 자동 생성 : 임의로 150000000부터 1씩 번호 증가
    def number():
        no = SendRecieveInfo.objects.count()
        if no == 0:
            return 150000000
        else:
            return no + 150000000

    #운송장 번호 : 택배기사모델과 연결
    ParcelNum = models.IntegerField(default=number, unique=True, primary_key=True)
    
    def __str__(self):
        return str(self.ParcelNum)

#택배, 택배기사 모델 : 택배에 대한 정보와 택배기사 정보 담겨있음
class DeliveryMan(models.Model):
    DeliveryMan_Name = models.CharField(max_length=50, default="홍길동")
    ManPhone = models.CharField(max_length=50, default="")
    ParcelNums = models.ForeignKey(
        SendRecieveInfo, 
        on_delete=models.CASCADE,
        related_name='SendRecieveInfo',
        null=True
    )
    Update_date = models.DateTimeField(auto_now_add = True)
    ParcelLocation = models.CharField(max_length=100, default="한국외대")
    ParcelStatus = models.CharField(max_length=100, default="배송 준비중")

    def __str__(self):
        return self.ParcelNums