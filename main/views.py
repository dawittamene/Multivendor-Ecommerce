from django.shortcuts import render
from rest_framework import generics, permissions, viewsets
# from rest_framework.pagination import LimitOffsetPagination
from main.models import *
from main.serializers import *
from .pagination import CustomLimitOffsetPagination


class VendorList(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    # permission_classes = [permissions.IsAuthenticated]
    
class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    # permission_classes = pagination.LimitOffsetPagination  
    
    
    
     
    # Product
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomLimitOffsetPagination 
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer    
    
    
    
    # Customer
class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    
class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer      
    
    
    # Order
class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
class OrderDetail(generics.ListCreateAPIView):
    serializer_class = OrderDetailSerializer

    def get_queryset(self):
        order_id = self.kwargs['pk']
        order = Order.objects.get(OrderId=order_id)
        order_items = OrderItem.objects.filter(order=order)
        return order_items
    
class CustomerAddressViewset(viewsets.ModelViewSet):
    queryset = CustomerAddress.objects.all()
    serializer_class = CustomerAddressSerializer

class ProductRatingViewset(viewsets.ModelViewSet):
    queryset = ProductRating.objects.all()
    serializer_class = ProductRatingSerializer
       
      