from django.contrib import admin


from main.models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ['user', 'address']
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price']
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']   
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user','mobile']    
    
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer','order_time']    
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order','product']    
    
class CustomerAddressAdmin(admin.ModelAdmin):
    list_display = ['address']   
class ProductRatingAdmin(admin.ModelAdmin):
    list_display = ['reviews','rating']                    


admin.site.register(Vendor, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(CustomerAddress, CustomerAddressAdmin)
admin.site.register(ProductRating, ProductRatingAdmin)
admin.site.register(ProductImage)







