# Generated by Django 3.2.6 on 2022-11-30 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_alter_product_price_from'),
        ('party_decoration', '0005_rename_party_decoration_balloon'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='balloon',
            new_name='party_decoration',
        ),
        migrations.RenameModel(
            old_name='balloon_sub_type',
            new_name='party_decoration_sub_type',
        ),
        migrations.RenameModel(
            old_name='balloon_type',
            new_name='party_decoration_type',
        ),
    ]
