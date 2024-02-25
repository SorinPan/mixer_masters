from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OOoRHI1Q9Jt1Iwh9JQ37f50V9HKPG4HVePe1kZvaigQyIzxt9PV97LULCLX50O4rfzrKMEmISu3h3XwUXFn8kUO00j2eDU542',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
