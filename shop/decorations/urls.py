from django.urls import path
from . import views

urlpatterns = [
    path('', views.decoration_en, name ="decoration"),
    path('cn/', views.decoration_cn, name="decoration cn"),
    path('type/<type_id>', views.decoration_type_en, name="decoration type"),
    path('type/cn/<type_id>', views.decoration_type_cn, name="decoration type cn"),
    path('details/<id>/', views.decoration_details_en, name="decoration details"),
    path('details/cn/<id>/', views.decoration_details_cn, name="decoration details cn"),
    path('post_main_type/', views.post_decoration_maintypes, name="decoration main type post"),
    path('post_sub_type/', views.post_decoration_subtypes, name="decoration sub type post"),

]