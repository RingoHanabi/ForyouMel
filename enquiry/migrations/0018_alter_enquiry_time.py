# Generated by Django 3.2.6 on 2021-11-06 08:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquiry', '0017_alter_enquiry_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 6, 19, 23, 3, 357654)),
        ),
    ]
