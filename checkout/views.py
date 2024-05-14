from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import CheckoutForm
from shopping_bag.contexts import shopping_bag_contents
import stripe 
from django.conf import settings

# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your shopping bag is  empty, please choose items to purchase")
        return redirect(reverse('products'))
    current_bag=shopping_bag_contents(request)
    total=current_bag['grand_total']
    stripe_total=round(total*100)
    checkout_form = CheckoutForm()
    template = 'checkout/checkout.html'
    context = {
        'checkout_form': checkout_form,
        'stripe_public_key': 'pk_test_51OzJsR09cBHepEM8cwk9sLwFJXb08KhYt32EiXPfiumpqcY83g0K2nlMoKTtwdVgtx5llQUZmmjaTXnUCHKLchfB00ZtCNCDQc',
        'client_secret': 'client_Secret',
    }
    return render(request, template, context)
