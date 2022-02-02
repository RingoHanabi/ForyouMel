# Generated by Django 3.2.6 on 2022-01-16 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0011_auto_20211213_1940'),
    ]

    operations = [
        migrations.CreateModel(
            name='decoration_type',
            fields=[
                ('type_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shop.type')),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['order'],
            },
            bases=('shop.type',),
        ),
        migrations.CreateModel(
            name='decoration_sub_type',
            fields=[
                ('type_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shop.type')),
                ('order', models.PositiveIntegerField(default=0)),
                ('main_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='decorations.decoration_type')),
            ],
            options={
                'ordering': ['order'],
            },
            bases=('shop.type',),
        ),
        migrations.CreateModel(
            name='decoration',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shop.product')),
                ('order', models.PositiveIntegerField(default=0)),
                ('main_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='decorations.decoration_type')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='decorations.decoration_sub_type')),
            ],
            options={
                'ordering': ['order'],
            },
            bases=('shop.product',),
        ),
    ]