from django.urls import path
from . import views

urlpatterns = [
    path('', views.enquiry, name="enquiry"),
    path('cn/', views.enquiry_cn, name="enquiry_cn")

]
