from django.urls import path
from . import views

urlpatterns = [
    path('flower/',views.flower),
    path('balloon/', views.balloon),
    path('party/', views.party),
    path('wedding/', views.wedding),

]