from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('cart/',views.CartView.as_view(),name='cart'),
    path('add-to-cart/<int:pk>/',views.add_to_cart, name='add_to_cart'),

   
]
