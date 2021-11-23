from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
from django.utils.safestring import mark_safe


class flower_type(models.Model):
    name_en = models.CharField(max_length=50, unique=True)
    name_cn = models.CharField(max_length=50, unique=True)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['order']

    def __str__(self):
        return self.name_cn


class flower(models.Model):
    name_en = models.CharField(max_length=50)
    name_cn = models.CharField(max_length=50)

    price = models.FloatField()
    description_en = models.TextField()
    description_cn = models.TextField()

    type = models.ForeignKey(flower_type, on_delete=models.DO_NOTHING)
    thumbnail = models.ImageField(upload_to="static/img/flowers/", default="image")
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    supplyment_image1 = models.ImageField(upload_to="static/img/flowers/", default="image")
    supplyment_image2 = models.ImageField(upload_to="static/img/flowers/", default="image")
    supplyment_image3 = models.ImageField(upload_to="static/img/flowers/", default="image")
    supplyment_image4 = models.ImageField(upload_to="static/img/flowers/", default="image")
    supplyment_image5 = models.ImageField(upload_to="static/img/flowers/", default="image")
    supplyment_image6 = models.ImageField(upload_to="static/img/flowers/", default="image")
    supplyment_image7 = models.ImageField(upload_to="static/img/flowers/", default="image")
    supplyment_image8 = models.ImageField(upload_to="static/img/flowers/", default="image")
    supplyment_image9 = models.ImageField(upload_to="static/img/flowers/", default="image")
    details_en = RichTextField(blank=True, null=True)
    details_cn = RichTextField(blank=True, null=True)

    class Meta(object):
        ordering = ['order']

    def __str__(self):
        return self.name_cn


    def thumbnail_image(self):
        return mark_safe("<img src='/{}' width='150'>".format(self.thumbnail))

