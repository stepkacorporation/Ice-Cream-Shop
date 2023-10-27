from django.test import TestCase

from ...forms import LoginUserForm
from ...models import UserProfile
from .utils.abstract_tests import AbstractCharFieldTest


class LoginUserFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        UserProfile.objects.create_user(username='existingusername', password='its a super hard password')

    def setUp(self) -> None:
        self.form_data = {'username': 'existingusername', 'password': 'its a super hard password'}


class LoginUserFormObjectTest(LoginUserFormTest):
    def test_object_field_order(self):
        form = LoginUserForm()
        expected_field_order = ('username', 'password')
        self.assertEqual(form.field_order, expected_field_order)

    def test_object_error_messages(self):
        form = LoginUserForm()
        expected_error_messages = {'invalid_login': 'Неправильный логин или пароль.', }
        self.assertEqual(form.error_messages, expected_error_messages)


class LoginUserFormUsernameTest(AbstractCharFieldTest, LoginUserFormTest):
    form = LoginUserForm
    field_name = 'username'
    placeholder = 'Имя пользователя'
    label = 'Username'
    required = True
    incorrect_values = []


class RegisterUserFormPassword1Test(AbstractCharFieldTest, LoginUserFormTest):
    form = LoginUserForm
    field_name = 'password'
    placeholder = 'Пароль'
    label = 'Пароль'
    required = True
    incorrect_values = []
