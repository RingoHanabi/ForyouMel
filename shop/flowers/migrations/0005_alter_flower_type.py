# Generated by Django 3.2.6 on 2021-12-13 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0004_flower_main_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flower',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flowers.flower_sub_type'),
        ),
    ]
