from django.contrib import admin

from .models import Product, Supplier


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


class SupplierAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)
admin.site.register(Supplier, SupplierAdmin)