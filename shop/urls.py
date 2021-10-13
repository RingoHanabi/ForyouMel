from django.urls import path
from . import views

urlpatterns = [
    path('flower/',views.flower, name = "flower"),
    path('balloon/', views.balloon, name = "balloon"),
    path('party/', views.party, name = "party"),
    path('wedding/', views.wedding, name = "wedding"),
    path('flower_cn/', views.flower_cn, name = "flower cn"),
    path('balloon_cn/', views.balloon_cn, name = "balloon cn"),
    path('party_cn/', views.party_cn, name = "party cn"),
    path('wedding_cn/', views.wedding_cn, name = "wedding cn"),

]