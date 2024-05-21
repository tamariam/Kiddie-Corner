from django.shortcuts import render, get_object_or_404,redirect
from products.models import Product
from .models import Favourite
from django.contrib import messages

# Create your views here.


def favourites(request):
    return render(request, 'favourites/favourites.html')


def add_to_favourite(request, product_id):
    '''view to add product in favourites
    '''
    product = get_object_or_404(Product, id=product_id)
    # Check if the product is already in favourites list 
    if Favourite.objects.filter(user=request.user, product=product).exists():
        messages.info(request, f'{product.name} is already in your favourites')
    else:
        Favourite.objects.create(user=request.user, product=product)
        messages.success(request, f'{product.name} has b een added to your favourites')
    return redirect('product_detail', product_id=product_id)
    


