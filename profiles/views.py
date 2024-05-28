from django.shortcuts import render, get_object_or_404
from .forms import UserProfileForm
from .models import UserProfile
from django.contrib import messages


# Create your views here.


def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    if request == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Profile Updated')
    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,


    }
    return render(request, 'profiles/profile.html', context)
