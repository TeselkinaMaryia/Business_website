from django.urls import path
from . import views
from .views import UserEditProfile, PasswordsChangeViews, ShopMain

urlpatterns = [
    path('', ShopMain.as_view(), name='shop'),
    path('brand/', views.shop_brand, name='brand'),
    path('<int:pk>/', views.goods_more, name='goods_more'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('search/', views.search_brand, name='search_brand'),
    path('edit_profile/', UserEditProfile.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeViews.as_view(template_name='registration/change_password.html')),
    path('password_success', views.password_success, name='password_success')
]

