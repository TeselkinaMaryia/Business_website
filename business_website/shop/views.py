from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.urls import reverse_lazy
from .forms import EditProfileForm, RegisterUserForm, PasswordChangingForm
from django.contrib.auth.views import PasswordChangeView
from . import models
from cart import forms


def shop_main(request):
    laptops = models.Laptops.objects.all().order_by('brand')
    context = {
        'laptops': laptops,
    }
    return render(request, 'shop/shop_main.html', context)


def shop_brand(request, brand):
    laptops = models.Laptops.objects.filter(brand__name__contains=brand)
    context = {
        'brand': brand,
        'laptops': laptops
    }
    return render(request, 'shop/brands.html', context)


def goods_more(request, pk):
    laptop = models.Laptops.objects.get(pk=pk)
    cart_laptop_form = forms.CartAddLaptop()
    context = {
        'laptop': laptop,
        'cart_laptop_form': cart_laptop_form
    }
    return render(request, 'shop/goods_more.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('shop')
        else:
            return redirect('login')
    else:
        return render(request, 'registration/login.html', )


def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('shop')
    else:
        form = RegisterUserForm()
    context = {
        'form': form
    }
    return render(request, 'registration/register.html', context)


def logout_user(request):
    logout(request)
    return redirect('shop')


def search_brand(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        laptops = models.Laptops.objects.filter(brand__name=searched)
        context = {
            'searched': searched,
            'laptops': laptops
        }
        return render(request, 'shop/searched_laptops.html', context)
    else:
        return render(request, 'shop/searched_laptops.html')


class UserEditProfile(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('shop')

    def get_object(self):
        return self.request.user


class PasswordsChangeViews(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')


def password_success(request):
    return render(request, 'registration/password_success.html')
