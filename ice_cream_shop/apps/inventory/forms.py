from django import forms

from .related_models.product_related_models import ProductBrand, ProductType, ProductManufacturer, ProductTaste


class ProductFilterForm(forms.Form):
    min_price = forms.DecimalField(min_value=0, required=False)
    max_price = forms.DecimalField(min_value=0, required=False)
    brands = forms.ModelMultipleChoiceField(queryset=ProductBrand.objects.all(), required=False)
    types = forms.ModelMultipleChoiceField(queryset=ProductType.objects.all(), required=False)
    min_weight = forms.DecimalField(min_value=0, required=False)
    max_weight = forms.DecimalField(min_value=0, required=False)
    manufacturers = forms.ModelMultipleChoiceField(queryset=ProductManufacturer.objects.all(), required=False)
    tastes = forms.ModelMultipleChoiceField(queryset=ProductTaste.objects.all(), required=False)