from django.shortcuts import render
from .models import Testimonial
# Create your views here.


def testimonials(request):
    """This view renders Testimonials page """
    testimonials = Testimonial.objects.all()
    return render(request, 'testimonials/testimonials.html',
                  {'testimonials': testimonials})
