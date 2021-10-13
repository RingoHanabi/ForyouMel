from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage),
    path('home_en/', views.homepage_en, name="homepage"),

    path('home_cn/', views.homepage_cn, name="homepage_cn")

]