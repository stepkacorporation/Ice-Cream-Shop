from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterUserForm, LoginUserForm


class RegisterUser(CreateView):
    """
    Класс представления для регистрации пользователей.
    """

    form_class = RegisterUserForm
    template_name = 'authentication/register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context

    def form_valid(self, form):
        """
        Создает учетную запись пользователя и выполняет вход после успешной валидации формы.
        """

        user = form.save()
        login(self.request, user)
        return redirect('catalog')  # Изменить на какую-то страницу


class LoginUser(LoginView):
    """
    Класс представления для аутентификации пользователей.
    """

    form_class = LoginUserForm
    template_name = 'authentication/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context

    def form_valid(self, form):
        """
        Выполняет вход в учетную запись пользователя после успешной валидации формы.
        """

        user = form.get_user()
        login(self.request, user)
        return redirect('catalog')


def logout_user(request):
    """
    Функция представления для завершения сессии пользователя.
    """

    logout(request)
    return redirect('catalog')
