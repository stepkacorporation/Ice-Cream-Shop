from django.db.models import ExpressionWrapper, Sum, DecimalField, F

from apps.orders.models import CartItem


class DataMixin:
    def get_user_context_data(self, **kwargs) -> dict:
        context = kwargs

        context['cart_total'] = self.get_cart_total(self.request) if self.request.user.is_authenticated else None
        context['cart_total_amount'] = self.get_cart_total_amount(self.request) if self.request.user.is_authenticated else None

        return context

    @staticmethod
    def get_cart_total(request) -> int:
        cart_total = CartItem.objects.filter(user=request.user).aggregate(total_quantity=Sum('quantity'))[
            'total_quantity']

        return cart_total if cart_total is not None else 0

    @staticmethod
    def get_cart_total_amount(request) -> int:
        cart_total_amount = CartItem.objects.filter(user=request.user) \
            .annotate(total_price=ExpressionWrapper(F('quantity') * F('product__price'), output_field=DecimalField())) \
            .aggregate(total_amount=Sum('total_price'))['total_amount']

        return cart_total_amount if cart_total_amount is not None else 0
