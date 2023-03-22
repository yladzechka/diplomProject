from django.shortcuts import redirect, render, get_object_or_404

from decimal import Decimal
from catalog.models import Product


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = request.session.get('cart', {})
    if product_id in cart:
        cart[int(product_id)]['quantity'] += 1
    else:
        cart[int(product_id)] = {
            'name': product.name,
            'price': str(product.price),
            'image': str(product.image),
            'quantity': 1
        }
    request.session['cart'] = cart
    return redirect('index')


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
    return redirect('cart')


def view_cart(request):
    cart = request.session.get('cart', {})
    products = Product.objects.all()
    params = {
        'products': products,
        'cart': cart,
    }
    return render(request, 'cart.html', params)
