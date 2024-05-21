from django.urls import path
from.views import favourites, add_to_favourite

urlpatterns = [
    path('', favourites, name='favourites'),
    path('add_to_favourite<int:product_id>/', add_to_favourite, name='add_to_favourite'),
    

]
