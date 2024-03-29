# Generated by Django 2.2.7 on 2019-12-06 06:06

from django.db import migrations, models
import django.db.models.deletion
import track_module.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SendRecieveInfo',
            fields=[
                ('Sender_Name', models.CharField(default='', max_length=100)),
                ('Sender_phone', models.CharField(default='', max_length=100)),
                ('Sender_addr', models.CharField(default='', max_length=100)),
                ('Sender_date', models.DateTimeField(auto_now_add=True)),
                ('Reciever_Name', models.CharField(default='', max_length=100)),
                ('Reciever_phone', models.CharField(default='', max_length=100)),
                ('Reciever_addr', models.CharField(default='', max_length=100)),
                ('ParcelNum', models.IntegerField(default=track_module.models.SendRecieveInfo.number, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryMan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DeliveryMan_Name', models.CharField(default='홍길동', max_length=50)),
                ('ManPhone', models.CharField(default='', max_length=50)),
                ('Update_date', models.DateTimeField(auto_now_add=True)),
                ('ParcelLocation', models.CharField(default='한국외대', max_length=100)),
                ('ParcelStatus', models.CharField(default='배송 준비중', max_length=100)),
                ('ParcelNums', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SendRecieveInfo', to='track_module.SendRecieveInfo')),
            ],
        ),
    ]
