from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cake/', views.cake, name='cake'),
    path('home/', views.home, name='home'),
    path('api/wishes/', views.api_wishes, name='api_wishes'),
    path('api/wishes/add/', views.api_add_wish, name='api_add_wish'),
]
