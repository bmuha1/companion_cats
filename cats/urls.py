from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='cats-home'),
    path('about/', views.about, name='cats-about'),
    path('all/', views.all, name='cats-all'),
    path('find/', views.find, name='cats-find'),
    path('cat/<cat_id>', views.cat, name='cats-cat')
    
    # path('random/', views.random, name='cats-random'),
    # path('add/', views.add, name='cats-add')
]
