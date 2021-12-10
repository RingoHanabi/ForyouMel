from django.urls import path
from . import views

urlpatterns = [
    path('', views.flower_en, name ="flower"),
    path('cn/', views.flower_cn, name="flower cn"),
    path('details/<id>/', views.flower_details_en, name="flower details"),
    path('details/cn/<id>/', views.flower_details_cn, name="flower details cn"),
    path('post_main_type/', views.post_flower_maintypes, name="flower main type post"),
    path('post_sub_type/', views.post_flower_subtypes, name="flower sub type post"),

]