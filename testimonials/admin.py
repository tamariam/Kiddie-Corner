from django.contrib import admin
from .models import Testimonial
# Register your models here.


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    """
    access the Testimonial fields model in Django Admin panel
    """
    list_display = (
        'name', 'profession',)
    search_fields = (
        'name',)

