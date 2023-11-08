from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView

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


class CartView(DataMixin, ListView):
    model = CartItem
    template_name = 'orders/cart.html'
    context_object_name = 'cart_items'

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        unique_item_count = CartItem.objects.filter(user=self.request.user).count()

        user_context = super().get_user_context_data(
            title='Корзина',
            unique_item_count=unique_item_count,
        )

        return context | user_context


def decrease_cart_item(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)

    if cart_item.quantity >= 1:
        cart_item.quantity -= 1
        cart_item.save()

    response_data = {
        'cart_item_quantity': cart_item.quantity,
        'cart_item_subtotal': cart_item.product.price * cart_item.quantity,
        'cart_total': DataMixin.get_cart_total(request),
        'cart_total_amount': DataMixin.get_cart_total_amount(request),
    }

    return JsonResponse(response_data)


def increase_cart_item(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)

    cart_item.quantity += 1
    cart_item.save()

    response_data = {
        'cart_item_quantity': cart_item.quantity,
        'cart_item_subtotal': cart_item.product.price * cart_item.quantity,
        'cart_total': DataMixin.get_cart_total(request),
        'cart_total_amount': DataMixin.get_cart_total_amount(request),
    }

    return JsonResponse(response_data)


def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()

    response_data = {
        'cart_total': DataMixin.get_cart_total(request),
        'cart_total_amount': DataMixin.get_cart_total_amount(request),
        'unique_item_count': CartItem.objects.filter(user=request.user).count(),
    }

    return JsonResponse(response_data)
