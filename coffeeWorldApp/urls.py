from django.urls import path
from . import views

urlpatterns = [
    path('', views.drink_list, name='drink_list'),
    path('post/bean/', views.bean_new, name='bean_new'),
]
