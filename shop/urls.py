from django.urls import path, include


urlpatterns = [
    path('flower/',include('shop.flowers.urls')),
    path('balloon/', include('shop.balloon.urls')),
    path('party/', include('shop.party_hire.urls')),
    path('wedding/', include('shop.wedding.urls')),

]