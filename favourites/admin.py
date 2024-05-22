from django.contrib import admin
from .models import Favourite

# Register your models here.


@admin.register(Favourite)
class FavouriteAdmin(admin.ModelAdmin):
    """
    access the Category fields model in Django Admin panel
    """
    list_display = (
        'user', 'product', 'added_on')
    search_fields = (
        'product',)

    readonly_fields = (
        'added_on',
    )
    
    ordering = ('-added_on',)
