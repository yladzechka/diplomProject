from django.shortcuts import render

from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, ListView

from catalog.models import Item


class MainView(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        items = Item.objects.all()
        new_items = Item.objects.all()[:4]
        sale_items = Item.objects.all().filter(discount_price__gt=0)
        params = {
            'items': items,
            'new_items': new_items,
            'sale_items': sale_items
        }
        return render(request, self.template_name, params)


class ThingView(TemplateView):
    template_name = 'thing.html'

    def get(self, request, id):
        item = Item.objects.get(id=id)
        params = {
            'item': item
        }
        return render(request, self.template_name, params)


class AllItemView(TemplateView):
    template_name = 'all_items.html'

    def get(self, request):
        items = Item.objects.all()
        params = {
            'items': items,
        }
        return render(request, self.template_name, params)


class SaleView(TemplateView):
    template_name = 'sale.html'

    def get(self, request):
        items = Item.objects.all().filter(discount_price__gt=0)
        params = {
            'items': items,
        }
        return render(request, self.template_name, params)

#
# class MaleView(TemplateView):
#     template_name = 'male.html'

    # def product_list(self, request):
    #     min_price = request.GET.get('min_price')
    #     max_price = request.GET.get('max_price')
    #     size = request.GET.get('size')
    #
    #     products = Item.objects.all()
    #
    #     if min_price:
    #         products = products.filter(price__gte=min_price)
    #     if max_price:
    #         products = products.filter(price__lte=max_price)
    #     if size:
    #         products = products.filter(size=size)
    #
    #     products = products.order_by('price', 'size')
    #
    #     return render(request, self.template_name, {'products': products})


class MaleView(ListView):
    model = Item
    template_name = 'male.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()

        # Filter by minimum price
        min_price = self.request.GET.get('min_price')
        if min_price:
            queryset = queryset.filter(price__gte=min_price)

        # Filter by maximum price
        max_price = self.request.GET.get('max_price')
        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        # Filter by size
        size = self.request.GET.get('size')
        if size:
            queryset = queryset.filter(size=size)

        return queryset

    # def product_list(request):
    #     min_price = request.GET.get('min_price')
    #     max_price = request.GET.get('max_price')
    #     size = request.GET.get('size')
    #
    #     products = Item.objects.all()
    #
    #     if min_price:
    #         products = products.filter(price__gte=min_price)
    #     if max_price:
    #         products = products.filter(price__lte=max_price)
    #     if size:
    #         products = products.filter(size=size)
    #
    #     products = products.order_by('price', 'size')
    #
    #     return render(request, 'product_list.html', {'products': products})
