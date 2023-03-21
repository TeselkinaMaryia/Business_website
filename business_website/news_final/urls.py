from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_main, name='news'),
    path('<int:pk>/', views.news_more, name='news_more'),
    path('events/', views.news_events, name='events'),
    path('events/<int:pk>/', views.events_more, name='events_more'),
    path('events/<category>/', views.events_category, name='events_category'),
    path('search/', views.search_news, name='search_news')
]
