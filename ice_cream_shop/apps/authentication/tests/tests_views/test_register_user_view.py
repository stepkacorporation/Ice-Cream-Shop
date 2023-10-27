from django.test import TestCase
from django.urls import reverse

from ...models import UserProfile
from ...forms import RegisterUserForm


class RegisterUserTest(TestCase):
    def setUp(self) -> None:
        self.user_data = {
            'first_name': 'FirstName',
            'last_name': 'LastName',
            'username': 'itsmyusername',
            'email': 'example@mail.ru',
            'password1': 'its a super hard password',
            'password2': 'its a super hard password',
        }

    def test_get_register_page(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], RegisterUserForm)
        self.assertTemplateUsed(response, 'authentication/register.html')
        self.assertEqual(response.context['title'], 'Регистрация')

    def test_post_valid_registration(self):
        user_data = self.user_data
        response = self.client.post(reverse('register'), user_data)
        # Ожидаем редирект после успешной регистрации
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('catalog'))
        # Проверяем создание пользователя
        self.assertTrue(UserProfile.objects.filter(username=user_data['username']).exists())

        # Проверяем, что пользователь залогинен
        logged_in = self.client.session.get('_auth_user_id')  # Проверяем, что ID пользователя находится в сессии
        self.assertTrue(logged_in is not None)

    def test_post_invalid_registration(self):
        user_data = self.user_data
        user_data['password1'] = 'mismatchedpassword'
        response = self.client.post(reverse('register'), user_data)
        # Ожидаем повторное отображение формы
        self.assertEqual(response.status_code, 200)
        # Убедимся, что пользователь не был создан
        self.assertFalse(UserProfile.objects.filter(username=user_data['username']).exists())
