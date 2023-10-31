from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView

from .password_forms import PasswordResetFormWithEmailPlaceholder, SetPasswordFormWithPasswordPlaceholder


class CustomPasswordResetView(PasswordResetView):
    form_class = PasswordResetFormWithEmailPlaceholder


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = SetPasswordFormWithPasswordPlaceholder
