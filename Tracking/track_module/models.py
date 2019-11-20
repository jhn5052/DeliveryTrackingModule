from django.db import models

# Create your models here.
class Sender(models.Model):
    Sender_Name = models.CharField(max_length=100, primary_key=True)
    Sender_Number = models.CharField(max_length=100)
    Sender_addr = models.CharField(max_length=100)
    Sender_date = models.DateField()

    def __str__(self):
        return self.Sender_Name


class Reciever(models.Model):
    Senders = models.ForeignKey(Sender, on_delete=models.CASCADE)
    Reciever_Name = models.CharField(max_length=100, primary_key=True)
    Reciever_Number = models.CharField(max_length=100)
    Reciever_addr = models.CharField(max_length=100)

    def __str__(self):
        return self.Reciever_Name


class Parcel(models.Model):
    Senders =  models.ForeignKey(Sender, on_delete=models.CASCADE)
    Recievers = models.ForeignKey(Reciever, on_delete=models.CASCADE)
    ParcelStatus = models.CharField(max_length=100)
    ParcelUpdate = models.BooleanField(blank=True) #택배 상태 update될 때
    ParcelStatus = models.CharField(max_length=100)
    ParcelNum = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.ParcelNum

class DeliveryMan(models.Model):
    Senders =  models.ForeignKey(Sender, on_delete=models.CASCADE)
    Recievers = models.ForeignKey(Reciever, on_delete=models.CASCADE) 
    Parcels = models.ManyToMany(
        Parcel,
        on_delete = CASCADE
    )
    ManName = models.CharField(max_length = 50)
    ManNum = models.CharField(max_length = 50)

    def __str__(self):
        return self.ManName