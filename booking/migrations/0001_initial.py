# Generated by Django 2.1.2 on 2018-11-12 15:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookingListIndi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_person', models.CharField(max_length=200)),
                ('industry_name', models.CharField(max_length=100)),
                ('date_visit', models.DateField(default=datetime.datetime(2018, 11, 12, 21, 1, 19, 622233))),
                ('slot_time', models.IntegerField(default=0)),
                ('visiting_members', models.IntegerField(default=0)),
                ('street_name', models.CharField(max_length=150)),
                ('city_name', models.CharField(max_length=100)),
                ('pin_code', models.CharField(max_length=10)),
                ('code', models.CharField(max_length=20)),
                ('visited', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='BookingListOrga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_person', models.CharField(max_length=200)),
                ('organisation_name', models.CharField(max_length=200)),
                ('industry_name', models.CharField(max_length=100)),
                ('date_visit', models.DateField(default=datetime.datetime(2018, 11, 12, 21, 1, 19, 623231))),
                ('slot_time', models.IntegerField(default=0)),
                ('visiting_members', models.IntegerField(default=0)),
                ('street_name', models.CharField(max_length=150)),
                ('city_name', models.CharField(max_length=100)),
                ('pin_code', models.CharField(max_length=10)),
                ('code', models.CharField(max_length=20)),
                ('visited', models.BooleanField(default=False)),
            ],
        ),
    ]
