from django.urls import path
from .views import shopping_bag, add_to_bag

urlpatterns = [
    path('', shopping_bag, name='shopping_bag'),
    path('', add_to_bag, name='add_to_bag'),
    path('add/<item_id>/', add_to_bag, name='add_to_bag'),
]