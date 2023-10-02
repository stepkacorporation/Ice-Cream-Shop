from django.db import models


class Income(models.Model):
    amount = models.PositiveIntegerField(verbose_name='Сумма  дохода (руб.)')
    description = models.TextField(verbose_name='Описание')
    date = models.DateField(auto_now_add=True, verbose_name='Дата дохода')

    def __str__(self):
        return f'{self.amount} руб. {self.date}'

    class Meta:
        verbose_name = 'Доход'
        verbose_name_plural = 'Доходы'
        ordering = ('-date',)


class Expense(models.Model):
    amount = models.PositiveIntegerField(verbose_name='Сумма  расхода (руб.)')
    description = models.TextField(verbose_name='Описание')
    date = models.DateField(auto_now_add=True, verbose_name='Дата расхода')

    def __str__(self):
        return f'{self.amount} руб. {self.date}'

    class Meta:
        verbose_name = 'Расход'
        verbose_name_plural = 'Расходы'
        ordering = ('-date', )

