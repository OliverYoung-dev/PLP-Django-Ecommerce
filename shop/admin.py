from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Product, Order, OrderItem

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'slug', 'image']
    prepopulated_fields = {'slug': ('name',)}