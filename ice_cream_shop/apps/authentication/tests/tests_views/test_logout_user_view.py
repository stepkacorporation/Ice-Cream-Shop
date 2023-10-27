from django.test import TestCase
from django.urls import reverse

from ...models import UserProfile


class LogoutUserTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        UserProfile.objects.create_user(username='itsmyusername', password='its a super hard password')

    def test_logout_user(self):
        self.client.login(username='itsmyusername', password='its a super hard password')

        response = self.client.get(reverse('logout'))
        # Проверяем что произошло перенаправление
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('catalog'))

        # Проверяем, что пользователь больше не аутентифицирован
        logged_in = self.client.session.get('_auth_user_id')
        self.assertTrue(logged_in is None)