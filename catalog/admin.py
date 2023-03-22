from django.contrib import admin
from .models import Category, Color, Product, Size

admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Product)
