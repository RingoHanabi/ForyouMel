from django.urls import path
from . import views

urlpatterns = [
    path('', views.wedding_floral_en, name = "wedding_floral_floral"),
    path('cn/', views.wedding_floral_cn, name = "wedding_floral_floral cn"),
    path('type/<type_id>', views.wedding_floral_type_en, name="wedding_floral_floral type"),
    path('type/cn/<type_id>', views.wedding_floral_type_cn, name="wedding_floral_floral type cn"),

    path('details/<id>/', views.wedding_floral_details_en, name="wedding_floral_floral details"),
    path('details/cn/<id>/', views.wedding_floral_details_cn, name="wedding_floral_floral details cn"),

]