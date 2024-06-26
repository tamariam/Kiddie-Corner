from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.shortcuts import HttpResponse
from django.contrib import messages
from .forms import CheckoutForm
from shopping_bag.contexts import shopping_bag_contents
import stripe
from django.conf import settings
from products.models import Product
from .models import Order, OrderLineItem
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from django.views.decorators.http import require_POST
import json


@require_POST
def cache_checkout_data(request):
    """
    This view  takes in the checkout data and
    stores it in the user's session
    """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    """
    This view that renders the checkout page and gets the
    payment form data from the profile
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }

        checkout_form = CheckoutForm(form_data)
        if checkout_form.is_valid():
            order = checkout_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            print('pid', pid)
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
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
            # save info to users profile
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success',
                                    args=[order.order_number]))
        else:
            messages.error('There is error in your Form,please '
                           'make sure everything is correct ')
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "Your shopping bag is  empty, "
                           "please choose items to purchase")
            return redirect(reverse('products'))
        current_bag = shopping_bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total*100)
        stripe.api_key = stripe_secret_key
        stripe_intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # Attempt to prefill the Profile form
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                checkout_form = CheckoutForm(initial={
                    'full_name': profile.default_name,
                    'email': profile.default_email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })

            except UserProfile.DoesNotExist:
                checkout_form = CheckoutForm()
        else:
            checkout_form = CheckoutForm()

        template = 'checkout/checkout.html'
        context = {
            'checkout_form': checkout_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': stripe_intent.client_secret,
        }
        return render(request, template, context)


def checkout_success(request, order_number):
    """
    This view that renders the checkout success page
    and saves shipping details to the profile if the
    user checks the save info box
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info is save info is checked
        if save_info:
            profile_data = {
                'default_name': order.full_name,
                'default_email': order.email,
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Your order processed successfully, '
                     f'a confirmation email will be sent to {order.email}')
    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    return render(request, template, {'order': order})
