from django.db import models

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


