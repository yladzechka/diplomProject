from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import ItemView, MainView, AllItemView, SaleView, MaleView, FemaleView

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('catalog/item-<int:id>/', ItemView.as_view(), name='catalog-item'),
    path('catalog/all-thing', ItemView.as_view(), name='catalog-all-thing'),
    path('new', AllItemView.as_view(), name='new'),
    path('sale', SaleView.as_view(), name='sale'),
    path('male', MaleView.as_view(), name='male'),
    path('male-filter/', views.male_filter, name='male-filter'),
    path('female', FemaleView.as_view(), name='female'),
    path('female-filter/', views.female_filter, name='female-filter')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
