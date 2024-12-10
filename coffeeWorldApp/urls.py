from django.urls import path
from . import views

urlpatterns = [
    path('', views.drink_list, name='drink_list'),
    path('order_confirmation/', views.order_confirmation, name='order_confirmation'),
    path('bean_list/', views.bean_list, name='bean_list'),
]
