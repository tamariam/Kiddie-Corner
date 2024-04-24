from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Category(models.Model):

    """
    models for product categories

    """

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254,  default='Untitled')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    in_stock = models.BooleanField(
        default=False, null=True, blank=True)
    favourite = models.ManyToManyField(
        User, related_name='favourite', blank=True)
    description = models.TextField(max_length=1024, default="")
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    rating = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True )
    has_sale = models.BooleanField(default=False)

    def __str__(self):
        return self.name


