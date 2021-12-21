from django.urls import path
from . import views

urlpatterns = [
    path('', views.flower_en, name ="flower"),
    path('cn/', views.flower_cn, name="flower cn"),
    path('type/<type_id>', views.flower_type_en, name="flower type"),
    path('type/cn/<type_id>', views.flower_type_cn, name="flower type cn"),
    path('details/<id>/', views.flower_details_en, name="flower details"),
    path('details/cn/<id>/', views.flower_details_cn, name="flower details cn"),
    path('post_main_type/', views.post_flower_maintypes, name="flower main type post"),
    path('post_sub_type/', views.post_flower_subtypes, name="flower sub type post"),

]