from django import forms
from .models import Cart

class AddToCartForm(forms.ModelForm):
    class Meta:
        model=Cart
        fields=["product_size","product_color","price"]