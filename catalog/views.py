from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, ListView
from catalog.models import Product

from .forms import ProductFilterForm


class MainView(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        products = Product.objects.all()
        new_products = Product.objects.all()[:4]
        cart = request.session.get('cart', {})
        sale_products = Product.objects.all().filter(discount_price__gt=0)[:4]
        params = {
            'products': products,
            'new_products': new_products,
            'sale_products': sale_products,
            'cart': cart,
        }
        return render(request, self.template_name, params)


class ItemView(TemplateView):
    template_name = 'item.html'

    def get(self, request, id):
        product = Product.objects.get(id=id)
        cart = request.session.get('cart', {})
        params = {
            'product': product,
            'cart': cart
        }
        return render(request, self.template_name, params)


class AllItemView(TemplateView):
    template_name = 'all_items.html'

    def get(self, request):
        products = Product.objects.all()
        cart = request.session.get('cart', {})
        params = {
            'products': products,
            'cart': cart
        }
        return render(request, self.template_name, params)


class SaleView(TemplateView):
    template_name = 'sale.html'

    def get(self, request):
        products = Product.objects.all().filter(discount_price__gt=0)
        cart = request.session.get('cart', {})
        params = {
            'products': products,
            'cart': cart
        }
        return render(request, self.template_name, params)


class MaleView(TemplateView):
    template_name = 'male.html'

    def get(self, request):
        queryset = Product.objects.all()
        filter_form = ProductFilterForm(request.GET)
        cart = request.session.get('cart', {})
        if filter_form.is_valid():
            min_price = filter_form.cleaned_data['min_price']
            max_price = filter_form.cleaned_data['max_price']
            size = filter_form.cleaned_data['size']
            if min_price:
                queryset = queryset.filter(price__gte=min_price)
            if max_price:
                queryset = queryset.filter(price__lte=max_price)
            if size:
                queryset = queryset.filter(size=size)
        context = {'queryset': queryset, 'filter_form': filter_form, 'cart': cart}
        return render(request, self.template_name, context)


def male_filter(request):
    products = Product.objects.all()

    min_price = request.GET.get('min_price')
    if min_price:
        products = products.filter(price__gte=min_price)

    max_price = request.GET.get('max_price')
    if max_price:
        products = products.filter(price__lte=max_price)

    size = request.GET.get('size')
    if size:
        products = products.filter(size__name=size)

    context = {
        'products': products,
        'filtered': True,
    }

    return render(request, 'male.html', context)


class FemaleView(TemplateView):
    template_name = 'female.html'

    def get(self, request):
        queryset = Product.objects.all()
        filter_form = ProductFilterForm(request.GET)
        cart = request.session.get('cart', {})
        if filter_form.is_valid():
            min_price = filter_form.cleaned_data['min_price']
            max_price = filter_form.cleaned_data['max_price']
            size = filter_form.cleaned_data['size']
            if min_price:
                queryset = queryset.filter(price__gte=min_price)
            if max_price:
                queryset = queryset.filter(price__lte=max_price)
            if size:
                queryset = queryset.filter(size=size)
        context = {'queryset': queryset,
                   'filter_form': filter_form,
                   'cart': cart}
        return render(request, self.template_name, context)


def female_filter(request):
    products = Product.objects.all()

    min_price = request.GET.get('min_price')
    if min_price:
        products = products.filter(price__gte=min_price)

    max_price = request.GET.get('max_price')
    if max_price:
        products = products.filter(price__lte=max_price)

    size = request.GET.get('size')
    if size:
        products = products.filter(size__name=size)

    context = {
        'products': products,
        'filtered': True,
    }

    return render(request, 'female.html', context)
