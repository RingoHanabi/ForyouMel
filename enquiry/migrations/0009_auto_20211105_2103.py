# Generated by Django 3.2.6 on 2021-11-05 10:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquiry', '0008_enquiry_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 5, 21, 3, 3, 528946)),
        ),
    ]