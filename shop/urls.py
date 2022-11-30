from django.urls import path, include


urlpatterns = [
    path('flower/',include('shop.flowers.urls')),
    path('party_decoration/', include('shop.party_decoration.urls')),
    path('party/', include('shop.party_hire.urls')),
    path('wedding_floral/', include('shop.wedding_floral.urls')),

]