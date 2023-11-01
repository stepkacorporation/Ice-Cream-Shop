from django.test import TestCase
from django.urls import reverse

from ...models import UserProfile


class LogoutUserTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        UserProfile.objects.create_user(username='itsmyusername', password='its a super hard password')

    def test_logout_user_post(self):
        self.client.login(username='itsmyusername', password='its a super hard password')

        response = self.client.post(reverse('logout'), {'logout_button': 'logout'})
        self.assertEqual(response.wsgi_request.method, 'POST')
        self.assertTrue('logout_button' in response.wsgi_request.POST)
        # Проверяем что произошло перенаправление
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('catalog'))

        # Проверяем, что пользователь больше не аутентифицирован
        logged_in = self.client.session.get('_auth_user_id')
        self.assertTrue(logged_in is None)

    def test_logout_user_get(self):
        self.client.login(username='itsmyusername', password='its a super hard password')

        response = self.client.get(reverse('logout'))

        # Проверяем что запрос был проигнорирован
        self.assertEqual(response.status_code, 204)

        # Проверяем, что пользователь все еще аутентифицирован
        logged_in = self.client.session.get('_auth_user_id')
        self.assertTrue(logged_in is not None)



