from django.urls import path
from.views import favourites, add_to_favourite,remove_favourite

urlpatterns = [
    path('', favourites, name='favourites'),
    path('add_to_favourite/<int:product_id>/', add_to_favourite, name='add_to_favourite'),
    path('remove_favourite/<int:product_id>/', remove_favourite, name='remove_favourite'),

    

]
