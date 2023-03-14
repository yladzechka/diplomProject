from django.urls import path, include
from . import views
from .views import ThingView, MainView, AllItemView, SaleView, MaleView

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('catalog/thing-<int:id>/', ThingView.as_view(), name='catalog-thing'),
    path('catalog/all-thing', ThingView.as_view(), name='catalog-all-thing'),
    path('new', AllItemView.as_view(), name='new'),
    path('sale', SaleView.as_view(), name='sale'),
    path('male', MaleView.as_view(), name='male'),

]
