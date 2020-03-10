from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='cats-home'),
    path('about/', views.about, name='cats-about'),
    path('random/', views.random, name='cats-random'),
    path('add/', views.add, name='cats-add')
]
