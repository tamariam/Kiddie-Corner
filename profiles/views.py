from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from .models import UserProfile
from django.contrib import messages
from checkout.models import Order


# Create your views here.

@login_required
# def profile(request):
#     if not request.user.is_superuser:
#         profile = get_object_or_404(UserProfile, user=request.user)
#         if request.method == 'POST':
#             form = UserProfileForm(request.POST, instance=profile)
#             if form.is_valid():
#                 form.save()
#                 messages.success(request, 'Your Profile Updated')
#             else:
#                 messages.error(request, 'invalid form sabmision')
#         else:
#             form = UserProfileForm(instance=profile)
#         orders = profile.orders.all()
#     else:
#         messages.error(request, 'ups')
#         context = {
#             'form': form,
#             'orders': orders,
#             'on_profile_page': True,
#         }
#     return render(request, 'profiles/profile.html', context)

def profile(request):
    if not request.user.is_superuser:
        profile = get_object_or_404(UserProfile, user=request.user)
        if request.method == 'POST':
            form = UserProfileForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your Profile Updated')
            else:
                messages.error(request, 'Invalid form submission')
        else:
            form = UserProfileForm(instance=profile)
        orders = profile.orders.all()
        context = {
            'form': form,
            'orders': orders,
            'on_profile_page': True,
        }
        return render(request, 'profiles/profile.html', context)
    else:
        messages.error(request, 'as a staff member you are not allowed to see this page')
        return redirect('home') 


def completed_order(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
                            f'''This is a past confirmation
                            for order number {order_number}. '''
                            'A confirmation email was sent on the order date.'
    ))

    context = {
        'order': order,
        'from_profile': True,
    }
    return render(request, 'checkout/checkout_success.html', context)
