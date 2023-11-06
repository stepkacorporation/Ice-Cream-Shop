from django.urls import path

from .views import ProductListView, ShowProductInfo

urlpatterns = [
    path('', ProductListView.as_view(), name='catalog'),
    path('<product_slug>/', ShowProductInfo.as_view(), name='product_info'),
]