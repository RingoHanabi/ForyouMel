from django.urls import path
from . import views

urlpatterns = [
    path('', views.party_decoration_en, name = "party_decoration"),
    path('cn/', views.party_decoration_cn, name = "party_decoration cn"),
    path('type/<type_id>', views.party_decoration_type_en, name="party_decoration type"),
    path('type/cn/<type_id>', views.party_decoration_type_cn, name="party_decoration type cn"),
    path('details/<id>/', views.party_decoration_details_en, name="party_decoration details"),
    path('details/cn/<id>/', views.party_decoration_details_cn, name="party_decoration details cn"),
    path('post_main_type/', views.post_party_decoration_maintypes, name="party_decoration main type post"),
    path('post_sub_type/', views.post_party_decoration_subtypes, name="party_decoration sub type post"),

]