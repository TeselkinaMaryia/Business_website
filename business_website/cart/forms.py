from django import forms
from . import models
from . import cart

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]
PAYMENT_CHOICE = [(1, 'in cash'), (2, 'by card')]
DELIVER = [(1, 'shop 1'), (2, 'shop 2'), (3, 'shop 3'), (4, 'shop 4'), (5, 'shop 5')]


class CartAddLaptop(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class OrderForm(forms.Form):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    address = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    delivery_address = forms.TypedChoiceField(choices=DELIVER, coerce=str)
    payment_method = forms.TypedChoiceField(choices=PAYMENT_CHOICE, coerce=str)

    class Meta:
        model = models.Order
        fields = ('first_name', 'last_name', 'email', 'address', 'delivery_address', 'payment_method')
