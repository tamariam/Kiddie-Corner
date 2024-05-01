from decimal import Decimal
from django.conf import settings


def shopping_bag_contents(request):
    bag_items = []
    total = 0
    count = 0

    if total < settings.FREE_SHIPPING_LIMIT:
        shipping = total * Decimal(settings.STANDARD_SHIPPING_PECRENT/100)
        free_shipping_delta = settings.FREE_SHIPPING_LIMIT - total
    else:
        shipping = 0
        free_shipping_delta = 0

    grand_total = shipping + total

    context = {
            'bag_items': bag_items,
            'total': total,
            'count':   count,
            'shipping': shipping,
            'free_shipping_delta': free_shipping_delta,
            'free_shipping_limit': settings.FREE_SHIPPING_LIMIT,
            'grand_total': grand_total

    }
    return context
