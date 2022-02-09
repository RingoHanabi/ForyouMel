from django.urls import path
from . import views

urlpatterns = [
    path('', views.balloon_en, name = "balloon"),
    path('cn/', views.balloon_cn, name = "balloon cn"),
    path('type/<type_id>', views.balloon_type_en, name="balloon type"),
    path('type/cn/<type_id>', views.balloon_type_cn, name="balloon type cn"),
    path('details/<id>/', views.balloon_details_en, name="balloon details"),
    path('details/cn/<id>/', views.balloon_details_cn, name="balloon details cn"),
    path('post_main_type/', views.post_balloon_maintypes, name="balloon main type post"),
    path('post_sub_type/', views.post_balloon_subtypes, name="balloon sub type post"),

]