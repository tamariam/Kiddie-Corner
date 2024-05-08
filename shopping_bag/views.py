from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product


def shopping_bag(request):
    return render(request, 'shopping_bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request,  f"{quantity} more { product.name }'s added to the bag")
    else:
        bag[item_id] = quantity

        messages.success(request,  f"{ bag[item_id] } { product.name }'s added to the bag")
    request.session['bag'] = bag
    return redirect(redirect_url)


def update_bag(request, item_id):
    """ up a quantity of the specified product to the shopping bag """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop[item_id]

    request.session['bag'] = bag
    return redirect(reverse('shopping_bag'))


def remove_item(request, item_id):
    """ up a quantity of the specified product to the shopping bag """
    bag = request.session.get('bag', {})
    if item_id in bag:
        del bag[item_id]

        request.session['bag'] = bag
        return redirect(reverse('shopping_bag'))
    else:
        return HttpResponse('ups',  status=404)
