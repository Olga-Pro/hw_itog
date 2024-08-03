from django import forms
from .models import Order

# Форма заказа


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        # fields = ['products']
        fields = ['status']
