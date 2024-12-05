from django.urls import path
from . import views

urlpatterns = [
    path('', views.drink_list, name='drink_list'),
    #path('coffeeWorld/<int:pk>/', views.drink_detail, name='drink_detail'),
    #path('coffeeWorld/new/', views.drink_new, name='drink_new'),
    #path('coffeeWorld/<int:pk>/edit/', views.drink_edit, name='drink_edit'),
]
