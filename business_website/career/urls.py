from django.urls import path
from . import views

urlpatterns = [
    path('', views.career_main, name='career'),
    path('vacancies/', views.vacancies, name='vacancies'),
    path('apply/', views.apply, name='apply'),
    path('vacancies/<int:pk>', views.vacancy_more, name='vacancy_more')
]