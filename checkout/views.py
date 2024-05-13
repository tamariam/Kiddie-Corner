from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import CheckoutForm

# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your shopping bag is  empty,choose items to purchase")
        return redirect(reverse('products'))
    checkout_form = CheckoutForm()
    template = 'checkout/checkout.html'
    return render(request, template, {'checkout_form': checkout_form})
