from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_main, name='about'),
    path('history/', views.about_history, name='history'),
    path('leadership/', views.about_leadership, name='leadership'),
    path('leadership/employee <int:pk>/', views.employees_more, name='employee'),
    path('leadership/senior employee <int:pk>/', views.senior_employees_more, name='senior employee')
]
