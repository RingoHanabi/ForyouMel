from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
from django.utils.safestring import mark_safe

from shop.models import Product, Type

class party_hire_type(Type):
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['order']

class party_hire_sub_type(Type):
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    main_type = models.ForeignKey(party_hire_type, on_delete=models.CASCADE)
    class Meta(object):
        ordering = ['order']

class party_hire(Product):
    main_type = models.ForeignKey(party_hire_type, on_delete=models.CASCADE)

    type = models.ForeignKey(party_hire_sub_type, on_delete=models.DO_NOTHING)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    class Meta(object):
        ordering = ['order']
