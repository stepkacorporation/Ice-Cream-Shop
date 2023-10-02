from django.db import models

#
# class BaseReport(models.Model):
#     title = models.CharField(max_length=255, verbose_name='Название')
#     description = models.TextField(verbose_name='Описание')
#     date_created = models.DateField(auto_now_add=True, verbose_name='Дата создания')
#     creator = models.ForeignKey('staff.Employee', on_delete=models.PROTECT, verbose_name='Создатель')
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         abstract = True
#
#
# class SalesReport(BaseReport):
#     sales_date = models.DateField(verbose_name='Дата продажи')
#     total_sales = models.PositiveIntegerField(verbose_name='Общая сумма продаж (руб.)')
#     products_sold = models.ManyToManyField('orders.OrderItem', related_name='sales_reports',
#                                            verbose_name='Проданные товары', blank=True)
