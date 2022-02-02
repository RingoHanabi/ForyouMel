from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
from django.utils.safestring import mark_safe

from shop.models import Product, Type

class decoration_type(Type):
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['order']

class decoration_sub_type(Type):
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    main_type = models.ForeignKey(decoration_type, on_delete=models.CASCADE)
    class Meta(object):
        ordering = ['order']



class decoration(Product):
    main_type = models.ForeignKey(decoration_type, on_delete=models.CASCADE, null=True)
    type = models.ForeignKey(decoration_sub_type, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    class Meta(object):
        ordering = ['order']
