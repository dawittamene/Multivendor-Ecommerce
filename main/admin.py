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


admin.site.register(Vendor, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Customer, CustomerAdmin)


