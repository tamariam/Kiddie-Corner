from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from .models import Favourite
from django.contrib import messages

# Create your views here.


def favourites(request):
    if not request.user.is_superuser:
        favourites = Favourite.objects.filter(user=request.user)
        return render(request, 'favourites/favourites.html', {'favourites': favourites})
    else:
        messages.info(request, 'as a staff member you are not allowed to view this page')
        return redirect('products')


def add_to_favourite(request, product_id):
    '''view to add product in favourites
    '''
    if not request.user.is_superuser:
        product = get_object_or_404(Product, id=product_id)
        # Check if the product is already in favourites list
        if Favourite.objects.filter(user=request.user, product=product).exists():
            messages.info(request, f'{product.name} is already in your favourites')
        else:
            Favourite.objects.create(user=request.user, product=product)
            messages.success(request, f'{product.name} has been added to your favourites')
        return redirect('favourites')
    else:
        messages.info(request,'ass a staff member you are not allowed to add products to the favourites')
        return redirect('home')



def remove_favourite(request, product_id):
    """Remove a product from the user's favourites"""
    product = get_object_or_404(Product, id=product_id)
    favourites = Favourite.objects.filter(user=request.user, product=product)
    messages.success(request, f'{product.name} has been removed from your favourites')

    if favourites.exists():
        favourites.delete()
    else:
        messages.warning(request, f' Can not find {product.name} in your favourites')
    return redirect('favourites')
