from django.urls import path
from . import views

urlpatterns = [
    path('', views.ask_main, name='ask'),

]
