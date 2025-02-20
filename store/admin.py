from django.contrib import admin
from store.models import Employee, Client, Provider, Category, Product, Order, Sale, SaleDetail

# Register your models here.
# admin.site.register(Employee)
# admin.site.register(Client)
# admin.site.register(Provider)
# admin.site.register(Category)
# admin.site.register(Product)
# admin.site.register(Order)
# admin.site.register(Sale)
# admin.site.register(SaleDetail)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'active']
    search_fields = ['name']
    
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'active', 'is_admin']
    search_fields = ['name', 'email', 'phone']
    
@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ['nit', 'name', 'address', 'email', 'phone', 'active']
    search_fields = ['nit', 'name', 'address', 'email', 'phone']
    
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'active', 'is_online']
    search_fields = ['name', 'email', 'phone']
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'active', 'category', 'provider']
    search_fields = ['name', 'price', 'stock']
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['date', 'provider', 'product', 'quantity', 'status', 'total']
    search_fields = ['date', 'provider', 'product', 'quantity', 'status', 'total']
    
@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ['date', 'client', 'employee', 'total']
    search_fields = ['date', 'client', 'employee']
    
@admin.register(SaleDetail)
class SaleDetailAdmin(admin.ModelAdmin):
    list_display = ['sale', 'product', 'quantity']
    search_fields = ['sale', 'product', 'quantity']