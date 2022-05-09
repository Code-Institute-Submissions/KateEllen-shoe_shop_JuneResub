from re import template
from tempfile import tempdir
from django.shortcuts import redirect, render, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag right now")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KxcSVH5svfFGlyI1C4VNdecGWIeSYSLivSJnb1l7SL0ybSJPITijycjsuR8vPg3HzkqMO61NB2GRod0POP8wjc400S55rHYO8',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)
