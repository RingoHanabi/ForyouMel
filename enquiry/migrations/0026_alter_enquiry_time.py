# Generated by Django 3.2.6 on 2021-11-24 04:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquiry', '0025_alter_enquiry_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 24, 15, 59, 27, 932039)),
        ),
    ]
