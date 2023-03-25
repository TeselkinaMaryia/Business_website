from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop import models
from .cart import Cart
from . import forms
from .models import OrderItem, Order


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


def cart_order(request):
    cart = Cart(request)
    form = forms.OrderForm()
    if request.method == 'POST':
        form = forms.OrderForm(request.POST)
        if form.is_valid():
            your_order = Order(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                address=form.cleaned_data['address'],
                payment_method=form.cleaned_data['payment_method'],
                delivery_address=form.cleaned_data['delivery_address'],
            )
            your_order.save()
            for item in cart:
                OrderItem.objects.create(order=your_order,
                                         laptop=item['laptop'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
    context = {
        'form': form,
        'cart': cart,
    }

    return render(request, 'cart/cart_order.html', context)
