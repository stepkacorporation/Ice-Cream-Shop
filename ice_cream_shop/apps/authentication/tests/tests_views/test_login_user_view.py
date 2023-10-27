from django.test import TestCase
from django.urls import reverse

from ...models import UserProfile
from ...forms import LoginUserForm


class RegisterUserTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        UserProfile.objects.create_user(username='itsmyusername', password='its a super hard password')

    def setUp(self) -> None:
        self.user_data = {'username': 'itsmyusername', 'password': 'its a super hard password'}

    def test_get_login_page(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], LoginUserForm)
        self.assertTemplateUsed(response, 'authentication/login.html')
        self.assertEqual(response.context['title'], 'Авторизация')

    def test_post_valid_login(self):
        user_data = self.user_data
        response = self.client.post(reverse('login'), user_data)
        # Ожидаем редирект после успешного входа
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('catalog'))

        # Проверяем, что пользователь залогинен
        logged_in = self.client.session.get('_auth_user_id')  # Проверяем, что ID пользователя находится в сессии
        self.assertTrue(logged_in is not None)

    def test_post_invalid_login(self):
        user_data = self.user_data
        user_data['password'] = 'wrongpassword'
        response = self.client.post(reverse('login'), user_data)
        # Ожидаем повторное отображение формы
        self.assertEqual(response.status_code, 200)
        # Убедимся, что пользователь не вошел в систему
        logged_in = self.client.session.get('_auth_user_id')
        self.assertTrue(logged_in is None)
