from rest_framework import serializers
from .models import *


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['UserId', 'user', 'address']
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['ProductId', 'name', 'detail', 'price']     
        
class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['ProductCategoryId', 'name', 'detail', 'price']           