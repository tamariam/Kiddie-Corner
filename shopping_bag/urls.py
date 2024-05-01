from django.urls import path
from .views import shopping_bag

urlpatterns = [
    path('', shopping_bag, name='shopping_bag'),
]
