from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from .models import Favourite
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def favourites(request):
    """This View renders favourites page"""
    if not request.user.is_staff:
        favourites = Favourite.objects.filter(user=request.user)
        return render(request, 'favourites/favourites.html',
                      {'favourites': favourites})
    else:
        messages.info(request, 'As a staff member you are '
                      'not allowed to view this page')
        return redirect('home')

@login_required
def add_to_favourite(request, product_id):
    '''view to add product in favourites
    '''
    if not request.user.is_staff:
        product = get_object_or_404(Product, id=product_id)
        # Check if the product is already in favourites list
        if Favourite.objects.filter(user=request.user,
                                    product=product).exists():
            messages.info(request, f'{product.name} '
                          f'is already in your favourites')
        else:
            Favourite.objects.create(user=request.user, product=product)
            messages.success(request, f'{product.name} has been added  '
                             f'to your favourites')
        return redirect('favourites')
    else:
        messages.info(request, 'As a staff member you are  '
                      ' not allowed to add products to the favourites')
        return redirect('home')


@login_required
def remove_favourite(request, product_id):
    """Remove a product from the user's favourites"""
    product = get_object_or_404(Product, id=product_id)
    favourites = Favourite.objects.filter(user=request.user, product=product)
    messages.success(request, f'{product.name} has been '
                     f'removed from your favourites')

    if favourites.exists():
        favourites.delete()
    else:
        messages.warning(request, f' Can not find {product.name}  '
                         f'in your favourites')
    return redirect('favourites')
