from django.urls import path
from . import views

urlpatterns = [
    path('', views.party_hire_en, name = "party_hire"),
    path('cn/', views.party_hire_cn, name = "party_hire cn"),
    path('details/<id>/', views.party_hire_details_en, name="party_hire details"),
    path('details/cn/<id>/', views.party_hire_details_cn, name="party_hire details cn"),

]