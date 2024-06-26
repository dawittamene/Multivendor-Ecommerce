from django.urls import path
from . import views

urlpatterns = [
    path('vendors/', views.VendorList.as_view()),
    path('vendor/<str:pk>/', views.VendorDetail.as_view()),
    
    path('products/', views.ProductList.as_view()),
    path('product/<str:pk>/', views.ProductDetail.as_view()),
    
    path('customers/', views.CustomerList.as_view()),
    path('customer/<str:pk>/', views.CustomerDetail.as_view()),
    
    path('orders/', views.OrderList.as_view()),
    path('order/<str:pk>/', views.OrderDetail.as_view()),
    
]
