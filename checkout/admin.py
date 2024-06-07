from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """
    Allows editing of line items in the admin
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    register  the Order model in Admin panel
    """
    inlines = (OrderLineItemAdminInline,)
    fields = (
        'order_number', 'full_name', 'date',
        'email', 'phone_number', 'country',
        'postcode', 'town_or_city', 'street_address1',
        'street_address2', 'county', 'shipping_cost',
        'order_total', 'grand_total',
        'order_status', 'shipping_method', 'original_bag', 'stripe_pid',
        'user_profile',
    )
    list_display = (
        'full_name', 'email', 'phone_number', 'order_number',
        'date', 'shipping_cost',
        'order_status', 'order_total', 'grand_total',
        'original_bag', 'stripe_pid',
        )
    search_fields = (
        'full_name', 'phone_number',
        'email', 'order_number',)

    readonly_fields = (
        'order_number', 'order_total', 'grand_total',
        'shipping_cost', 'original_bag', 'date'

    )

    list_filter = (
        'order_number',  'full_name', 'shipping_method', 'date'
    )

    ordering = ('-date',)
