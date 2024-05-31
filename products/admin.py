from django.contrib import admin
from .models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    access the Category fields model in Django Admin panel
    """
    list_display = (
        'friendly_name', 'name',)
    search_fields = (
        'friendly_name', 'name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    access the Product fields model in Admin panel
    """
    list_display = (
        'id',
        'name', 'category', 'description', 'in_stock',
        'rating',
        'price', 'sku', 'image',)
    search_fields = (
        'category', 'name',
        'price', 'rating',)
