from django.urls import path
from . import views

urlpatterns = [
    path('', views.balloon_en, name = "balloon"),
    path('cn/', views.balloon_cn, name = "balloon cn"),
    path('details/<id>/', views.balloon_details_en, name="balloon details"),
    path('details/cn/<id>/', views.balloon_details_cn, name="balloon details cn"),

]