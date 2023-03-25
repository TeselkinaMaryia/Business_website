from django.urls import path
from .views import AskMain
from . import views

urlpatterns = [
    path('', AskMain.as_view(), name='ask'),
    path('<category>/', views.all_question, name='all_questions'),
    path('<category>/<int:pk>/', views.all_comments, name='all_comments')
]
