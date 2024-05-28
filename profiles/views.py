from django.shortcuts import render, get_object_or_404
from .forms import UserProfileForm
from .models import UserProfile

# Create your views here.


def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    form = UserProfileForm(instance=profile)
    context = {
        'form': form,


    }
    return render(request, 'profiles/profile.html', context)
