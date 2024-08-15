from django.shortcuts import render
from rest_framework import generics, permissions, viewsets
# from rest_framework.pagination import LimitOffsetPagination
from main.models import *
from main.serializers import *
from .pagination import CustomLimitOffsetPagination
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate

class VendorList(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    # permission_classes = [permissions.IsAuthenticated]
    
class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    # permission_classes = pagination.LimitOffsetPagination  
    
    
class CategoryList(generics.ListCreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CustomLimitOffsetPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        category_param = self.request.query_params.get('category')

        if category_param:
            try:
                category_uuid = UUID(category_param)
            except ValueError:
                raise ValidationError(f"'{category_param}' is not a valid UUID.")

            queryset = queryset.filter(id=category_uuid)

        return queryset

    
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CustomLimitOffsetPagination
    
    

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomLimitOffsetPagination
    
    def get_queryset(self):
        qs = super().get_queryset()
        if 'category' in self.request.GET:
            category=self.request.GET['category']
            category=ProductCategory.objects.get(id=category)
            qs = qs.filter(category=category)
        return qs
    
class TagProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomLimitOffsetPagination
    
    def get_queryset(self):
        qs = super().get_queryset()
        tag=self.kwargs['tag']
        qs = qs.filter(tags__icontains=tag)
        return qs
    
class RelatedProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomLimitOffsetPagination
    
    def get_queryset(self):
        qs = super().get_queryset()
        product_id=self.kwargs['pk']
        product=Product.objects.get(id=product_id)
        qs = qs.filter(category=product.category).exclude(id=product_id)
        return qs    
        
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer    
    
    
    
    # Customer
class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    pagination_class = CustomLimitOffsetPagination 
    
    
class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer      
    
    
    # Order
class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = CustomLimitOffsetPagination 
    
    
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
       
      
      
    # auth
@csrf_exempt    
def Customerlogin(request):
    email=request.POST.get('email')
    password=request.POST.get('password')
    user=authenticate(email=email, password=password)
    if user:
        msg={
            'bool':True,
            'user':user.email
        }
    else:
         msg={
            'bool':False,
            'user':'invalid email/password'
        }    
    
    return JsonResponse(mes)     
        