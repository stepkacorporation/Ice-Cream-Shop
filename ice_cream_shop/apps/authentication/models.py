from django.contrib.auth.models import AbstractUser, Permission
from django.db import models


class UserProfile(AbstractUser):
    email = models.EmailField(unique=True)
    user_groups = models.ManyToManyField('UserGroup', verbose_name='Группы', blank=True)
    points = models.PositiveIntegerField(default=0, verbose_name='Баллы', blank=True)
    email_is_verified = models.BooleanField(default=False, verbose_name='Подтвержденный email', blank=True)
    email_verification_token = models.CharField(max_length=255, verbose_name='Email-токен', blank=True, null=True)
    last_email_verification_request = models.DateTimeField(verbose_name='Дата последней отправки email пользователю', blank=True, null=True)

    def __str__(self):
        return self.username


class UserGroup(models.Model):
    name = models.CharField(max_length=80, unique=True, verbose_name='Имя')
    permissions = models.ManyToManyField(Permission, blank=True, verbose_name='Права')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
