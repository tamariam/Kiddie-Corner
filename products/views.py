from django.shortcuts import render, redirect, reverse
from .models import Product,Category
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.db.models import Q


def all_products(request):
    products = Product.objects.all()
    query = None
    category_filter = None  # Initialize category filter variable
    has_sale_filter = request.GET.get('has_sale')

    if has_sale_filter == 'True':
        products = products.filter(has_sale=True)

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, 'Please enter what you are looking for.')
                return redirect(reverse('products'))

            # Define filter criteria for search query
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

        if 'category' in request.GET:
            category_filter = request.GET['category']
            if category_filter:  # Ensure category filter is not empty
                # Filter products by category
                products = products.filter(category__name=category_filter)

    # Retrieve all categories for rendering in template
        categories = Category.objects.all()
   
    context = {
        'products': products,
        'categories': categories,  # Pass all categories to template
        'query': query,
        'category_filter': category_filter,  # Pass category filter value to template
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    context = {
      'product':product,
    }

    return render(request, 'products/product_detail.html',  context)
