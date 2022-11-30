from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
from django.utils.safestring import mark_safe

from shop.models import Type, Product


class party_decoration_type(Type):
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['order']



class party_decoration_sub_type(Type):
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    main_type = models.ForeignKey(party_decoration_type, on_delete=models.CASCADE)

    class Meta(object):
        ordering = ['order']

class party_decoration(Product):
    main_type = models.ForeignKey(party_decoration_type, on_delete=models.CASCADE, null=True)
    sub_type = models.ForeignKey(party_decoration_sub_type, on_delete=models.CASCADE, null = True)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    supplyment_image10 = models.ImageField(upload_to="static/img/flowers/", default="image")
    supplyment_image11 = models.ImageField(upload_to="static/img/flowers/", default="image")
    supplyment_image12 = models.ImageField(upload_to="static/img/flowers/", default="image")
    supplyment_image13 = models.ImageField(upload_to="static/img/flowers/", default="image")
    supplyment_image14 = models.ImageField(upload_to="static/img/flowers/", default="image")
    supplyment_image15 = models.ImageField(upload_to="static/img/flowers/", default="image")
    supplyment_image16 = models.ImageField(upload_to="static/img/flowers/", default="image")
    supplyment_image17 = models.ImageField(upload_to="static/img/flowers/", default="image")
    supplyment_image18 = models.ImageField(upload_to="static/img/flowers/", default="image")
    supplyment_image19 = models.ImageField(upload_to="static/img/flowers/", default="image")

    class Meta(object):
        ordering = ['order']
