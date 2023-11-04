from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Product, Supplier, StockEntry
from .related_models.product_related_models import ProductBrand, ProductType, ProductSupplements,\
    ProductTypeOfPackaging, ProductFeatures, ProductStandard, ProductTaste, ProductProducingCountry, \
    ProductManufacturer


class ProductAdmin(ImportExportModelAdmin):
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
admin.site.register(ProductBrand, ImportExportModelAdmin)
admin.site.register(ProductType, ImportExportModelAdmin)
admin.site.register(ProductSupplements, ImportExportModelAdmin)
admin.site.register(ProductTypeOfPackaging, ImportExportModelAdmin)
admin.site.register(ProductFeatures, ImportExportModelAdmin)
admin.site.register(ProductStandard, ImportExportModelAdmin)
admin.site.register(ProductTaste, ImportExportModelAdmin)
admin.site.register(ProductProducingCountry, ImportExportModelAdmin)
admin.site.register(ProductManufacturer, ImportExportModelAdmin)