from django.urls import path
from . import views

urlpatterns = [
    path('', views.wedding_en, name = "wedding"),
    path('cn/', views.wedding_cn, name = "wedding cn"),
    path('details/<id>/', views.wedding_details_en, name="wedding details"),
    path('details/cn/<id>/', views.wedding_details_cn, name="wedding details cn"),

]