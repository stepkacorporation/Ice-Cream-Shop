from django.contrib import admin

from .models import Product, Supplier, StockEntry
from .related_models.product_related_models import ProductBrand, ProductType, ProductSupplements,\
    ProductTypeOfPackaging, ProductFeatures, ProductStandard, ProductTaste, ProductProducingCountry, \
    ProductManufacturer


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


class SupplierAdmin(admin.ModelAdmin):
    pass


class StockEntryAdmin(admin.ModelAdmin):
    pass


# models
admin.site.register(Product, ProductAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(StockEntry, StockEntryAdmin)

# product_related_models.py
admin.site.register(ProductBrand)
admin.site.register(ProductType)
admin.site.register(ProductSupplements)
admin.site.register(ProductTypeOfPackaging)
admin.site.register(ProductFeatures)
admin.site.register(ProductStandard)
admin.site.register(ProductTaste)
admin.site.register(ProductProducingCountry)
admin.site.register(ProductManufacturer)