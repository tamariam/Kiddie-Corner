from django.shortcuts import render

# Create your views here.


def testimonials(request):
    return render(request, 'testimonials/testimonials.html')