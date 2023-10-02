from django.contrib.auth.models import User
from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    # Изменить здесь модель User на новую модель пользователя
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Username')
    position = models.ForeignKey('Position', on_delete=models.PROTECT, verbose_name='Должность')
    phone = models.CharField(max_length=15, verbose_name='Телефон')
    email = models.EmailField(max_length=255, verbose_name='Эл. почта')
    hire_date = models.DateField(auto_now_add=True, verbose_name='Дата приема на работу')

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.position}'

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'
        ordering = ('last_name', )


class Position(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    salary = models.PositiveIntegerField(verbose_name='Зарплата (руб.)')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
        ordering = ('title', )


class Task(models.Model):
    TASK_STATUS = (
        ('pending', 'Ожидает выполнения'),
        ('processing', 'В процессе'),
        ('completed', 'Выполнена'),
    )

    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, verbose_name='Работник')
    due_date = models.DateField(verbose_name='Дата выполнения')
    status = models.CharField(max_length=15, choices=TASK_STATUS, default='pending', verbose_name='Статус')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ('-due_date', )
