from django.urls import path
from .views import profile, completed_order

urlpatterns = [
    path('', profile, name='profile'),
    path('completed_order/<order_number>', completed_order, name='completed_orders'),
]