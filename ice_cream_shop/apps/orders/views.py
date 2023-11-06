from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

from ..inventory.models import Product
from ..inventory.utils import DataMixin
from .models import CartItem


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = CartItem.objects.get_or_create(user=request.user, product=product)
    cart.quantity += 1
    cart.save()

    product_info = {
        'product_name': product.name,
    }

    cart_info = {
        'cart_total': DataMixin.get_cart_total(request),
        'cart_total_amount': DataMixin.get_cart_total_amount(request)
    }

    return JsonResponse(product_info | cart_info)


def remove_from_cart(request, cart_item_id):
    pass


def view_cart(request):
    pass
