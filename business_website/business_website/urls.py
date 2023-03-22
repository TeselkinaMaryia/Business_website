"""business_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_page, name='main page'),
    path('about/', include('about.urls'), name='about'),
    path('news/', include('news_final.urls'), name='news'),
    path('career/', include('career.urls'), name='career'),
    path('ask/', include('ask.urls'), name='ask'),
    path('shop/', include('django.contrib.auth.urls')),
    path('shop/', include('shop.urls'), name='shop'),
    path('cart/', include('cart.urls'), name='cart')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
