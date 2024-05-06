from django.db import models
from django.contrib.auth.models import User
import uuid

class Vendor(models.Model):
    UserId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField(null=True)
    
    def __str__(self):
        return self.user.username
    
class ProductCategory(models.Model):
    ProductCategoryId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    detail = models.TextField(null=True)
    
    def __str__(self):
        return self.name    
    
class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True, related_name='category_product')
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)
    
    ProductId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    detail = models.TextField(null=True)
    price = models.FloatField()
    
    
    def __str__(self):
        return self.name        
    
# customer Model
class Customer(models.Model):
    CustomerId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.PositiveBigIntegerField()
    
    def __str__(self):
        return self.user.username
    
    
class Order(models.Model):
    customer =  models.ForeignKey(Customer, on_delete=models.CASCADE)    
    order_time = models.DateTimeField(auto_now_add=True)   


class OrderItem(models.Model):
    order =  models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')  
    product =  models.ForeignKey(Customer, on_delete=models.CASCADE)  
    
    def __str__(self):
        return self.product.name
    
    
    

        
