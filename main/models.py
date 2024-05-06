from django.db import models
from django.contrib.auth.models import User
import uuid


class Vendor(models.Model):
    UserId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField(null=True)
    
    def __str__(self):
        return self.user
    
class Product(models.Model):
    ProductId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    detail = models.TextField(null=True)
    price = models.FloatField()
    
    def __str__(self):
        return self.name        
    
class ProductCategory(models.Model):
    ProductCategoryId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    detail = models.TextField(null=True)
    
    def __str__(self):
        return self.name
    

        
