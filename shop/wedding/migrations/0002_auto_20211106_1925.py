# Generated by Django 3.2.6 on 2021-11-06 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='balloon',
            name='type',
        ),
        migrations.DeleteModel(
            name='balloon_type',
        ),
        migrations.RemoveField(
            model_name='flower',
            name='type',
        ),
        migrations.RemoveField(
            model_name='partyhire',
            name='type',
        ),
        migrations.DeleteModel(
            name='partyhire_type',
        ),
        migrations.AlterField(
            model_name='weddingdecoration',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='wedding.weddingdecoration_type'),
        ),
        migrations.DeleteModel(
            name='balloon',
        ),
        migrations.DeleteModel(
            name='flower',
        ),
        migrations.DeleteModel(
            name='flower_type',
        ),
        migrations.DeleteModel(
            name='partyhire',
        ),
    ]
