from django.urls import path

from .views import add_to_cart, remove_from_cart, view_cart

urlpatterns = [
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:cart_item_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/', view_cart, name='cart'),
]