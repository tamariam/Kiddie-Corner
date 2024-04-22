from django.db import models


# Create your models here.


class Category(models.Model):

    """
    models for product categories

    """

    name = models.CharField(max_length=254)
    friendly_name = models.Charfield(max_ength=254, null=True, black=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
