from django.contrib import admin
from django.urls import path, include

from shopping_cart import views

urlpatterns = [
    path('en/', views.shopping_cart_en, name = "shopping cart en"),
    path('cn/', views.shopping_cart_cn, name = "shopping cart cn"),
    path('checkout/', views.checkout_en, name = "checkout en"),
    path('checkout/cn/', views.checkout_cn, name = "checkout cn"),
]
