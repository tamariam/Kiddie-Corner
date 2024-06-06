from django.shortcuts import render, redirect, reverse
from .models import Product, Category
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .forms import ProductForm


def all_products(request):
    """This View renders all products  """
    products = Product.objects.all()
    query = None
    category_filter = None
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
            queries = (
                    Q(name__icontains=query) |
                    Q(description__icontains=query)
            )
            products = products.filter(queries)

        if 'category' in request.GET:
            category_filter = request.GET['category']
            if category_filter:
                # Filter products by category
                products = products.filter(category__name=category_filter)

    categories = Category.objects.all()

    context = {
        'products': products,
        'categories': categories,
        'query': query,
        'category_filter': category_filter,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """This view renders product detail page"""
    product = get_object_or_404(Product, pk=product_id)

    context = {
      'product': product,
    }

    return render(request, 'products/product_detail.html',  context)


@login_required
def add_product(request):
    """ view to add product
    """
    if request.user.is_staff:
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                product = form.save()
                messages.success(request, 'Product added successfully')
                return redirect(reverse('product_detail',  args=[product.id]))
            else:
                messages.error(
                    request,
                    'Faild product submission, please make '
                    'sure the form is valid and try again'
                    )
        else:
            form = ProductForm()
        return render(request, 'products/add_product.html', {'form': form})
    else:
        messages.error(request, 'You are not allowed to view this page')
        return redirect('home')


@login_required
def edit_product(request, product_id):
    """ view to add product
    """
    if request.user.is_staff:
        product = get_object_or_404(Product, pk=product_id)
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES, instance=product)
            if form.is_valid():
                form.save()
                messages.success(request, 'Product edited successfully')
                return redirect(reverse('product_detail',  args=[product.id]))
            else:
                messages.error(
                    request,
                    'Faild product update, please '
                    'make sure the form is valid and try again'
                    )
        else:
            form = ProductForm(instance=product)
        return render(
                    request,
                    'products/edit_product.html',
                    {'form': form, 'product': product})
    else:
        messages.error(
                       request,
                       'You are not allowed '
                       'to change  product details'
                    )
        return redirect('home')


@login_required
def delete_product(request, product_id):
    """ delete product view"""
    if request.user.is_staff:
        product = get_object_or_404(Product, pk=product_id)
        product.delete()
        messages.success(
                        request,
                        f" Product  {product.name} successsfully deleted"
                    )
        return redirect(reverse('products'))
    else:
        messages.error(request, 'You are not allowed to delete product')
