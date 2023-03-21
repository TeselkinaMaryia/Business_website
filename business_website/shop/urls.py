from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_main, name='shop'),
    path('brand/', views.shop_brand, name='brand'),
    path('<int:pk>/', views.goods_more, name='goods_more'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('search/', views.search_brand, name='search_brand')
]

# accounts/ login/ [name='login']
# accounts/ logout/ [name='logout']
# accounts/ password_change/ [name='password_change']
# accounts/ password_change/done/ [name='password_change_done']
# accounts/ password_reset/ [name='password_reset']
# accounts/ password_reset/done/ [name='password_reset_done']
# accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/ reset/done/ [name='password_reset_complete']
