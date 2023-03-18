from django.urls import path, include
from . import views
from .views import ItemView, MainView, AllItemView, SaleView, MaleView

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('catalog/item-<int:id>/', ItemView.as_view(), name='catalog-item'),
    path('catalog/all-thing', ItemView.as_view(), name='catalog-all-thing'),
    path('new', AllItemView.as_view(), name='new'),
    path('sale', SaleView.as_view(), name='sale'),
    path('male', MaleView.as_view(), name='male'),
    path('male-filter/', views.male_filter, name='male-filter')
]
