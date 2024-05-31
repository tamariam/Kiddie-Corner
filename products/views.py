from django.shortcuts import render, redirect, reverse
from .models import Product, Category
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .forms import ProductForm


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
                messages.error(request, 'what you are looking for?')
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
      'product': product,
    }

    return render(request, 'products/product_detail.html',  context)


def add_product(request):
    """ view to add product
    """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'product added successfully')
            return redirect(reverse('product_detail',  args=[product]))
        else:
            messages.error(request, 'faild product submission, please make sure the form is valid and try again')
    else:
        form = ProductForm()
    
    return render(request, 'products/add_product.html', {'form': form})


def edit_product(request, product_id):
    """ view to add product
    """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'product edited successfully')
            return redirect(reverse('product_detail',  args=[product.id]))
        else:
            messages.error(request, 'faild product update, please make sure the form is valid and try again')
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'products/edit_product.html', {'form': form, 'product': product})


def delete_product(request, product_id):
    """ up a quantity of the specified product to the shopping bag """
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request,  f" { product.name } successsfully removed  from your bag")
    return redirect(reverse('products'))
