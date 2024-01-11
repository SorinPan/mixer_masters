from django.shortcuts import render


def view_cart(request):
    """ 
    A view that renders the content of the shopping cart 
    """

    return render(request, 'cart/cart.html')
