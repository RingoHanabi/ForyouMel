from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe


class Type(models.Model):
    name_en = models.CharField(max_length=50, unique=True)
    name_cn = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name_cn


class Product(models.Model):
    name_en = models.CharField(max_length=50, null=True)
    name_cn = models.CharField(max_length=50, null=True)
    price = models.FloatField(null=True)
    description_en = models.TextField(null=True)
    description_cn = models.TextField(null=True)
    thumbnail = models.ImageField(upload_to="static/img/flowers/", default="image")
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

    def __str__(self):
        return self.name_cn

    def thumbnail_image(self):
        return mark_safe("<img src='/{}' width='150'>".format(self.thumbnail))


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField()

    def __str__(self):
        return self.name


class ShoppingCart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)


class ShoppingCartItem(models.Model):
    shopping_cart = models.ForeignKey(ShoppingCart, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=0)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, null=True, blank=True)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    shopping_cart = models.ForeignKey(ShoppingCart, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=0)
