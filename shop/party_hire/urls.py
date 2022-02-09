from django.urls import path
from . import views

urlpatterns = [
    path('', views.party_hire_en, name = "party_hire"),
    path('cn/', views.party_hire_cn, name = "party_hire cn"),
    path('type/<type_id>', views.party_hire_type_en, name="party_hire type"),
    path('type/cn/<type_id>', views.party_hire_type_cn, name="party_hire type cn"),

    path('details/<id>/', views.party_hire_details_en, name="party_hire details"),
    path('details/cn/<id>/', views.party_hire_details_cn, name="party_hire details cn"),
    path('post_main_type/', views.post_party_hire_maintypes, name="party_hire main type post"),
    path('post_sub_type/', views.post_party_hire_subtypes, name="party_hire sub type post"),

]