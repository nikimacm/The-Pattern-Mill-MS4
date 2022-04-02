from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KkC1GAjEPNREPT2lRaQ99sqDP896gFy8UH0IicC2QDwc8Tq24FSdrwjZ6eo7Eh49HXaFl1dnr5DbSnko3apN2EZ00FIeo2nW3',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
