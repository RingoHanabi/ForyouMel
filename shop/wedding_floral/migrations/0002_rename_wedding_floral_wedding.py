# Generated by Django 3.2.6 on 2022-11-30 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_alter_product_price_from'),
        ('wedding_floral', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='wedding_floral',
            new_name='wedding',
        ),
    ]
