from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Favourite(models.Model):
    """
    Model for favourites
    """
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='users_favourites')
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='favourited_by')
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ''' Ensure a user can't add the
        same product to theirfavourites multiple times '''
        unique_together = ('user', 'product')

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
