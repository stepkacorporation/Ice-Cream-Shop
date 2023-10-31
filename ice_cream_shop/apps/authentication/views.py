from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils import timezone
from django.views.generic import CreateView

from .forms import RegisterUserForm, LoginUserForm

from .services.email_manager.token_utils import get_token_by_username
from .services.email_manager.send_email import send_an_email_to_confirm_email


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
        Создает учетную запись пользователя, генерирует токен и отправляет ссылку на электронный
        адрес пользователя для подтверждения его email, далее выполняет вход в аккаунт.
        """

        user = form.save(commit=False)

        token = get_token_by_username(user.username)
        user.email_verification_token = token
        user.last_email_verification_request = timezone.now()

        send_an_email_to_confirm_email(user, token)

        user.save()
        login(self.request, user)
        return redirect('catalog')

    def get(self, request, *args, **kwargs):
        """
        Проверяет, если пользователь уже вошел в аккаунт, то переадресовываем его на страницу каталога.
        """

        if self.request.user.is_authenticated:
            return redirect('catalog')
        return super().get(request, *args, **kwargs)


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

    def get(self, request, *args, **kwargs):
        """
        Проверяет, если пользователь уже вошел в аккаунт, то переадресовываем его на страницу каталога.
        """
        if self.request.user.is_authenticated:
            return redirect('catalog')
        return super().get(request, *args, **kwargs)


def logout_user(request):
    """
    Функция представления для завершения сессии пользователя.

    Если метод запроса - POST, если в данных POST-запроса присутствует ключ 'logout_button' и
    если пользователь уже авторизован, то сеанс пользователя завершается, и пользователь
    перенаправляется на страницу 'catalog'.

    Если пользователь не авторизован, но остальные условия выполнились корректно, то мы добавляем
    ему сообщение об ошибке, и переадресовываем его на ту же страницу, с которой был отправлен запрос.
    Если получить предыдущую страницу не удалось, то пользователь перенаправляется на страницу каталога.

    Если условия не выполняются (например, это GET-запрос или POST-запрос без 'logout_button'),
    функция возвращает HTTP-ответ со статусом 204, что означает успешную обработку без возврата
    какого-либо контента.
    """

    if request.method == 'POST' and 'logout_button' in request.POST:
        if request.user.is_authenticated:
            logout(request)
            return redirect('catalog')
        messages.error(request, 'Вы не вошли в систему, поэтому невозможно выполнить выход.')
        url = request.META.get('HTTP_REFERER', 'catalog')
        return redirect(url)

    return HttpResponse(status=204)
