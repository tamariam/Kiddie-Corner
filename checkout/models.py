from django.db import models
import uuid
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from products.models import Product

# Create your models here.


class Order(models.Model):
    ORDER_STATUS = (
        ('Received', 'Order Received'),
        ('Processing', 'Order Processing'),
        ('Dispatched', 'Order Dispatched'),
        ('On Hold', 'On Hold'),
        ('Cancelled', 'order Cancelled'),
    )

    SHIPPING_METHOD = (
            ('Standard', 'Standard Shipping'),
            ('Registered', 'Registered Shipping'),
            ('Free', 'Free Shipping'),
        )

    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=10, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    shipping_cost = models.DecimalField(max_digits=10,
                                        decimal_places=2,
                                        null=False, default=0)
    shipping_method = models.CharField(max_length=20, choices=SHIPPING_METHOD, null=False, blank=False, default='standard')                                  
    order_total = models.DecimalField(max_digits=10,
                                      decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10,
                                      decimal_places=2, null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    order_status = models.CharField(max_length=50, null=False, choices=ORDER_STATUS, default='received')


