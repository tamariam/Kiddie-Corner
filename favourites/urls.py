from django.urls import path
from.views import favourites

urlpatterns = [
    path('', favourites, name='favourites'),
]
