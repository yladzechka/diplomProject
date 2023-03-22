from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    total_products = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']


