from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .forms import CheckoutForm
from shopping_bag.contexts import shopping_bag_contents
import stripe 
from django.conf import settings
from products.models import Product
from .models import Order, OrderLineItem

# Create your views here.


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})
        form_data={
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'eircode': request.POST['eircode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        

    if not bag:
        messages.error(request, "Your shopping bag is  empty, please choose items to purchase")
        return redirect(reverse('products'))
    current_bag = shopping_bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total*100)
    stripe.api_key = stripe_secret_key
    stripe_intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )
    checkout_form = CheckoutForm()
    template = 'checkout/checkout.html'
    context = {
        'checkout_form': checkout_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': stripe_intent.client_secret,
    }
    return render(request, template, context)
