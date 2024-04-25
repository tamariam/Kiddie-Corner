from django.shortcuts import render
from .models import Product
from django.shortcuts import get_object_or_404

def all_products(request):
    products = Product.objects.all()

    context = {
      'products':products,
    }

    return render(request, 'products/products.html',  context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    context = {
      'product':product,
    }

    return render(request, 'products/product_detail.html',  context)
