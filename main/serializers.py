from rest_framework import serializers
from .models import *


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['UserId', 'user', 'address']
    def __init__(self, *args, **kwargs):
        super(VendorSerializer, self). __init__( *args, **kwargs)
        self.Meta.depth = 1    
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['ProductId','category','vendor', 'name', 'detail', 'price',]     
    def __init__(self, *args, **kwargs):
        super(ProductSerializer, self). __init__( *args, **kwargs)
        self.Meta.depth = 1
            
        
        
class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['ProductCategoryId', 'name', 'detail', 'price']   
    def __init__(self, *args, **kwargs):
        super(ProductCategorySerializer, self). __init__( *args, **kwargs)
        self.Meta.depth = 1            
        
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['CustomerId', 'user', 'mobile']       
    def __init__(self, *args, **kwargs):
        super(CustomerSerializer,self). __init__( *args, **kwargs)
        self.Meta.depth = 1
        
         
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['OrderId','customer']    
    def __init__(self, *args, **kwargs):
        super(OrderSerializer,self). __init__( *args, **kwargs)
        self.Meta.depth = 1     
        
class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['OrderItemId','order', 'product']     
    def __init__(self, *args, **kwargs):
        super(OrderDetailSerializer,self). __init__( *args, **kwargs)
        self.Meta.depth = 1          
        
class CustomerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerAddress
        fields = ['customeraddressId','customer', 'address']     
    def __init__(self, *args, **kwargs):
        super(CustomerAddressSerializer,self). __init__( *args, **kwargs)
        self.Meta.depth = 1             