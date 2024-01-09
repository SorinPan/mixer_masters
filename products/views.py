from django.shortcuts import render
from .models import Product, Category

def all_products(request):
    """ A view to return all products on the site """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
