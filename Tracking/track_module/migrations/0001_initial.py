# Generated by Django 2.2.7 on 2019-11-28 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sender',
            fields=[
                ('Sender_Name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Sender_phone', models.CharField(max_length=100)),
                ('Sender_addr', models.CharField(max_length=100)),
                ('Sender_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reciever',
            fields=[
                ('Reciever_Name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Reciever_phone', models.CharField(max_length=100)),
                ('Reciever_addr', models.CharField(max_length=100)),
                ('Senders', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='track_module.Sender')),
            ],
        ),
        migrations.CreateModel(
            name='Parcel',
            fields=[
                ('ParcelUpdate', models.BooleanField(blank=True)),
                ('ParcelStatus', models.CharField(max_length=100)),
                ('Parcelnum', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Recievers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='track_module.Reciever')),
                ('Senders', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='track_module.Sender')),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryMan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ManName', models.CharField(max_length=50)),
                ('ManPhone', models.CharField(max_length=50)),
                ('Parcels', models.ManyToManyField(to='track_module.Parcel')),
                ('Recievers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='track_module.Reciever')),
                ('Senders', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='track_module.Sender')),
            ],
        ),
    ]
