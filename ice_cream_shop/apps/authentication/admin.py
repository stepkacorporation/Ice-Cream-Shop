from django.contrib import admin
from django.contrib.auth.models import Group

from .models import UserProfile, UserGroup


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'points', 'is_verified', 'is_staff')
    fieldsets = (
        ('Основная информация', {
            'fields': ('first_name', 'last_name', 'username', 'password', 'email', 'user_groups', 'user_permissions'),
        }),
        ('Дополнительно', {
            'fields': ('is_active', 'is_verified', 'is_staff', 'is_superuser', 'date_joined', 'last_login'),
        }),
    )
    filter_horizontal = ('user_permissions',)


class UserGroupAdmin(admin.ModelAdmin):
    filter_horizontal = ('permissions',)


admin.site.unregister(Group)

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserGroup, UserGroupAdmin)
