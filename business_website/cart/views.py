from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop import models
from .cart import Cart
from . import forms


@require_POST
def cart_add(request, pk):
    cart = Cart(request)
    laptop = get_object_or_404(models.Laptops, pk=pk)
    form = forms.CartAddLaptop(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(laptop=laptop,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])

    return redirect('cart')


def cart_remove(request, pk):
    cart = Cart(request)
    laptop = get_object_or_404(models.Laptops, pk=pk)
    cart.remove(laptop)
    return redirect('cart')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart_detail.html', {'cart': cart})
