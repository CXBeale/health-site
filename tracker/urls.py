from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('food/', views.food_list, name='food_list'),
    path('food/add/', views.food_create, name='food_add'),
]