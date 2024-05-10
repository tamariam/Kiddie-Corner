django.db.models.signals.post_save, post_delete

from django.dispatch import receiver

from .models import OrderLineItem


def update_on_save(sende, instance, created, **kwargs):
    """
    Update order total when a lineitem as added
    or created.
    """
    instance.order.update.total()
