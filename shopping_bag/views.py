from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product


def shopping_bag(request):
    if not request.user.is_superuser:
        return render(request, 'shopping_bag/bag.html')
    else:
        messages.info(request,'as a staff member you are not allowed to see this page')
        return redirect('home') 


def add_to_bag(request, item_id):
    if not request.user.is_superuser:
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
    else:
        messages.info(request,'ass a staff member you are not allowed to add items in bage')
        return redirect('home') 



def update_bag(request, item_id):
    """ up a quantity of the specified product to the shopping bag """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        if item_id in bag:
            if bag[item_id] == quantity:
                messages.error(request, f"{quantity} {product.name}'s  is already  in the bag.please choose another quantity")
            else:
                bag[item_id] = quantity
                messages.success(request, f"{product.name}'s quantity updated to {quantity} in the bag.")
        else:
            messages.error(request, "Product not found in the bag.")
    else:
        messages.error(request, "Invalid quantity.")

    request.session['bag'] = bag
    return redirect(reverse('shopping_bag'))


def remove_item(request, item_id):
    """ up a quantity of the specified product to the shopping bag """
    product = get_object_or_404(Product, pk=item_id)
    bag = request.session.get('bag', {})
    if item_id in bag:
        del bag[item_id]
        messages.success(request,  f" { product.name } successsfully removed  from your bag")

        request.session['bag'] = bag
        return redirect(reverse('shopping_bag'))
    else:
        return HttpResponse('ups',  status=404)
