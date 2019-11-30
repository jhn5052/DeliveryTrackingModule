# Generated by Django 2.2.7 on 2019-11-30 19:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import track_module.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SendRecieveInfo',
            fields=[
                ('Sender_Name', models.CharField(default='null', max_length=100)),
                ('Sender_phone', models.CharField(default='null', max_length=100)),
                ('Sender_addr', models.CharField(default='null', max_length=100)),
                ('Sender_date', models.DateField(auto_now=True)),
                ('Reciever_Name', models.CharField(default='null', max_length=100)),
                ('Reciever_phone', models.CharField(default='null', max_length=100)),
                ('Reciever_addr', models.CharField(default='null', max_length=100)),
                ('ParcelNum', models.IntegerField(default=track_module.models.SendRecieveInfo.number, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Parcel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ParcelUpdate', models.BooleanField(default=True)),
                ('ParcelStatus', models.CharField(default='배송 준비중', max_length=100)),
                ('ParcelNum', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='track_module.SendRecieveInfo')),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryMan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ManPhone', models.CharField(default='null', max_length=50)),
                ('ParcelNum', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='track_module.SendRecieveInfo')),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
