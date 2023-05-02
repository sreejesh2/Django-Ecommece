from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [

   path('',views.IndexView.as_view(),name='home'),
   path('category/all/',views.CategoryView.as_view(),name='category'),
   path('category/<int:pk>/product/all/',views.ProductListView.as_view(),name='products'),
   path('product/<int:pk>/',views.ProductDetailView.as_view(),name='product-detail')


   
]
