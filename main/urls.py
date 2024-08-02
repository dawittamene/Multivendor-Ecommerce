from django.urls import path

from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('address', views.CustomerAddressViewset)
router.register('productrating', views.ProductRatingViewset)

urlpatterns = [
    path('vendors/', views.VendorList.as_view(), name='vendor-list'),
    path('vendor/<str:pk>/', views.VendorDetail.as_view(), name='vendor-detail'),
    path('products/', views.ProductList.as_view(), name='product-list'),
    path('products/<str:tag>/', views.TagProductList.as_view(), name='tag-list'),
    
    path('product/<str:pk>/', views.ProductDetail.as_view(), name='product-detail'),
    path('related-product/<str:pk>/', views.RelatedProductList.as_view(), name='relatedProductList'),
    
    
    path('categories/', views.CategoryList.as_view(), name='category-list'),
    path('category/<str:pk>/', views.CategoryDetail.as_view(), name='category-detail'),
    
    path('customers/', views.CustomerList.as_view(), name='customer-list'),
    path('customer/<str:pk>/', views.CustomerDetail.as_view(), name='customer-detail'),
    
    path('orders/', views.OrderList.as_view(), name='order-list'),
    path('order/<str:pk>/', views.OrderDetail.as_view(), name='order-detail'),
    
    
]


# Include the static media files configuration

urlpatterns += router.urls

