from django.contrib import admin
from .models import UserMessage


@admin.register(UserMessage)
class UserMessageAdmin(admin.ModelAdmin):
    """
    access the UserMessage fields model in Django Admin panel
    """
    fields = (
        'name', 'email', 'sent_on', 'status',
        'message', 'subject',

    )
    list_display = (
        'name', 'email', 'sent_on', 'status', 'subject',)
    search_fields = (
        'email''name',)

    readonly_fields = (
        'sent_on', 'name',
        'email', 'subject', 'message',
    )

    ordering = ('-sent_on',)
