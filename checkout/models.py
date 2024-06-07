from django.db import models
import uuid
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField
from decimal import Decimal

from products.models import Product
from profiles.models import UserProfile

# Create your models here.


class Order(models.Model):
    """"
    Model to keep a record of all customer orders
    """

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
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name="orders")
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
    shipping_method = models.CharField(max_length=20, choices=SHIPPING_METHOD,
                                       null=False, blank=False,
                                       default='standard')
    order_total = models.DecimalField(max_digits=10,
                                      decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10,
                                      decimal_places=2, null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    order_status = models.CharField(max_length=50, null=False,
                                    choices=ORDER_STATUS,
                                    default='received')
    stripe_pid = models.CharField(max_length=254, null=False,
                                  blank=False, default='')

    class Meta:
        ordering = ('-date',)

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """"
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """

        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0

        if self.order_total < settings.FREE_SHIPPING_LIMIT:

            self.shipping_cost = self.order_total * \
                Decimal(settings.STANDARD_SHIPPING_PECRENT / 100)

        else:

            self.shipping_cost = 0
            self.shipping_method = 'free'

        self.grand_total = self.order_total + self.shipping_cost
        self.save()

    def save(self, *args, **kwargs):
        """"
        add order number if there is not.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """ Model for current customer order item """
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    product = models.ForeignKey(Product, null=False,
                                blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False,
                                   blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6,
                                         decimal_places=2, null=False,
                                         blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Set lineitem total and update the order total.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'
