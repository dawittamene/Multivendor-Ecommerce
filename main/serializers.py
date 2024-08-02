from rest_framework import serializers
from .models import *


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(VendorSerializer, self). __init__( *args, **kwargs)
        self.Meta.depth = 1    
        
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id','product', 'image']
                        
                                
class ProductSerializer(serializers.ModelSerializer):
    product_rating = serializers.StringRelatedField(many=True, read_only=True)
    product_image = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id','name','image','slug','price','category','vendor','detail','tags','product_rating','product_image','tag_list']



        
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(CategorySerializer, self). __init__( *args, **kwargs)
        self.Meta.depth = 1         
        
# class CategoryDetaliSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductCategory
#         fields = '__all__'
#     def __init__(self, *args, **kwargs):
#         super(CategoryDetaliSerializer, self). __init__( *args, **kwargs)
#         self.Meta.depth = 1            
        
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'  
    def __init__(self, *args, **kwargs):
        super(CustomerSerializer,self). __init__( *args, **kwargs)
        self.Meta.depth = 1
        
         
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__' 
    def __init__(self, *args, **kwargs):
        super(OrderSerializer,self). __init__( *args, **kwargs)
        self.Meta.depth = 1     
        
class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'     
    def __init__(self, *args, **kwargs):
        super(OrderDetailSerializer,self). __init__( *args, **kwargs)
        self.Meta.depth = 1          
        
class CustomerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerAddress
        fields = '__all__'    
    def __init__(self, *args, **kwargs):
        super(CustomerAddressSerializer,self). __init__( *args, **kwargs)
        self.Meta.depth = 1 


class ProductRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductRating
        fields = '__all__'  
    def __init__(self, *args, **kwargs):
        super(ProductRatingSerializer,self). __init__( *args, **kwargs)
        self.Meta.depth = 1                      