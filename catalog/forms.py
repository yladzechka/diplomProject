from django import forms


class ProductFilterForm(forms.Form):
    min_price = forms.DecimalField(min_value=0, required=False)
    max_price = forms.DecimalField(min_value=0, required=False)
    size = forms.ChoiceField(choices=[('', 'All sizes'), ('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], required=False)
