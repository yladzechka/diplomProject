from django.urls import path
from . import views


urlpatterns = [
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('', views.view_cart, name='cart'),
    # path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
]
