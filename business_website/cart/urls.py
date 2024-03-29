from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_detail, name='cart'),
    path('add/<int:pk>', views.cart_add, name='cart_add'),
    path('remove/<int:pk>', views.cart_remove, name='cart_remove'),
    path('order/', views.cart_order, name='order')
]
