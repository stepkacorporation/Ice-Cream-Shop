from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from apps.authentication.models import UserProfile
from .validators import username_validator, first_name_validator, last_name_validator


class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(attrs={'placeholder': 'Ваше имя'}),
        validators=[first_name_validator]
    )
    last_name = forms.CharField(
        label='Фамилия',
        widget=forms.TextInput(attrs={'placeholder': 'Ваша фамилия'}),
        validators=[last_name_validator]
    )
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={'placeholder': 'Имя пользователя'}),
        validators=[username_validator]
    )
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    password2 = forms.CharField(
        label='Повторите пароль',
        widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'})
    )

    field_order = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))

    field_order = ('username', 'password')
    error_messages = {'invalid_login': 'Неправильный логин или пароль.', }
