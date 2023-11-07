from django.urls import path

from .views import add_to_cart, remove_from_cart, CartView

urlpatterns = [
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:cart_item_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/', CartView.as_view(), name='cart'),
]