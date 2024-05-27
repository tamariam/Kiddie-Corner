from django.urls import path
from .views import testimonials

urlpatterns = [
    path('', testimonials, name='testimonials'),
]
