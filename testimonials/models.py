from django.db import models
# from cloudinary.models import CloudinaryField

# Create your models here.


class Testimonial(models.Model):
    name = models.CharField(max_length=100,  blank=False, null=False)
    profession = models.CharField(max_length=254, blank=False, null=False)
    testimonial = models.TextField()
    featured_image = models.ImageField(null=True, blank=True)
    

    def __str__(self):
        return self.name
