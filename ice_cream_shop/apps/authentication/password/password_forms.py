from django import forms
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm


class PasswordResetFormWithEmailPlaceholder(PasswordResetForm):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'placeholder': 'Введите ваш email'}),
    )


class SetPasswordFormWithPasswordPlaceholder(SetPasswordForm):
    new_password1 = forms.CharField(
        label='Новый пароль',
        widget=forms.PasswordInput(attrs={'placeholder': 'Новый пароль'})
    )
    new_password2 = forms.CharField(
        label='Подтверждение нового пароля',
        widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'})
    )
