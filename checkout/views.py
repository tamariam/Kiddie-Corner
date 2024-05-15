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
        
        checkout_form = CheckoutForm(form_data)  
        if checkout_form.is_valid():
            checkout_form.save()
            order = checkout_form.save(commit=False)
            
            for item_id, quantity in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=quantity,
                    )
                    order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        """
                        One of the products in your bag wasn't
                        found in our database.
                    
                        """)
                    )
                    order.delete()
                    return redirect(reverse('shopping_bag'))
            
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success.html', args=[order.order_number]))
        else:
            messages.error('There is error in your Form,please make sure everything is correct ')
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


def checkout_success(request, order_number):
    '''successfull checkouts'''
    save_info = request.session.get('save-info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Your order processed successfully, a confirmation email will be sent to{order.email}')
    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    return render(request, template, {'order': order})




