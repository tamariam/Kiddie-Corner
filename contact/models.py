from django.db import models

# Choises for usermessage status
STATUS = (
    ("pending", "Pending"), ("done", "Done"),
    )


class UserMessage(models.Model):
    '''Model for Contact page
    '''
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    sent_on = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=50, null=False)
    message = models.TextField(max_length=250, null=False, blank=False)
    status = models.CharField(max_length=20, choices=STATUS, default="pending")

    def __str__(self):
        return f"{self.name} "
