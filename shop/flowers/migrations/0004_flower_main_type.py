# Generated by Django 3.2.6 on 2021-12-08 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0003_rename_type_flower_sub_type_main_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='flower',
            name='main_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='flowers.flower_type'),
        ),
    ]