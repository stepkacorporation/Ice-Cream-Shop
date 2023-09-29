from django.contrib.auth.models import User
from django.db import models


class Order(models.Model):
    ORDER_STATUS = (
        ('pending', 'Ожидание'),
        ('processing', 'В обработке'),
        ('completed', 'Выполнен'),
        ('canceled', 'Отменен'),
    )

    # Изменить здесь модель User на новую модель пользователя
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')
    order_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время заказа')
    status = models.CharField(max_length=12, choices=ORDER_STATUS, default='pending', verbose_name='Статус')
    total_cost = models.PositiveIntegerField(default=0, verbose_name='Стоимость заказа (руб.)')

    def __str__(self):
        return f'{self.pk}. {self.user}, {self.order_datetime}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ('-id', '-order_datetime')


class OrderItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, verbose_name='Заказ')
    product = models.ForeignKey('inventory.Product', on_delete=models.PROTECT, verbose_name='Продукт')
    quantity = models.PositiveIntegerField(verbose_name='Кол-во')
    subtotal = models.PositiveIntegerField(default=0, verbose_name='Стоимость позиции (руб.)')

    def save(self, *args, **kwargs):
        self.subtotal = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.order} {self.product} {self.quantity} шт.'

    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказа'
        ordering = ('-id', )
