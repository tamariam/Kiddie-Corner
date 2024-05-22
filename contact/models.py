from django.db import models


class UserMessage(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    sent_on = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=50, null=False)
    message = models.TextField(max_length=250, null=False, blank=False)
    pending = models.BooleanField(default=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} "


