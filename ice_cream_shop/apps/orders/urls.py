from django.urls import path

from .views import add_to_cart, remove_from_cart, CartView, increase_cart_item, decrease_cart_item

urlpatterns = [
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:cart_item_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/', CartView.as_view(), name='cart'),
    path('increase/<int:cart_item_id>/', increase_cart_item, name='increase_cart_item'),
    path('decrease/<int:cart_item_id>/', decrease_cart_item, name='decrease_cart_item'),
    path('remove/<int:cart_item_id>/', remove_from_cart, name='remove_cart_item'),
]