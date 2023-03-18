from django.shortcuts import redirect, render, get_object_or_404

from decimal import Decimal
from catalog.models import Product


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = request.session.get('cart', {})
    if product_id in cart:
        cart[product_id]['quantity'] += 1
    else:
        cart[product_id] = {
            'name': product.name,
            'price': str(product.price),
            'image': str(product.image),
            'quantity': 1
        }
    request.session['cart'] = cart
    return redirect('index')


# def remove_from_cart(request, product_id: int):
#     cart = request.session.get('cart', {})
#     if product_id in cart:
#         del cart[product_id]
#         request.session['cart'] = cart
#     return redirect('cart')
def remove_from_cart(request, product_id):
    product_id = Product.objects.get(id=product_id)
    cart = request.session.get('cart', {})
    if product_id:
        if product_id in cart:
            del cart[product_id]
            request.session['cart'] = cart
    return redirect('cart')

def view_cart(request):
    cart = request.session.get('cart', {})
    context = {'cart': cart}
    return render(request, 'cart.html', context)
