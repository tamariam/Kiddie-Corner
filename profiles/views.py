from django.shortcuts import render

# Create your views here.


def profile(request):
    """this View displays user profile content
    """

    return render(request, "profiles/profile.html")

