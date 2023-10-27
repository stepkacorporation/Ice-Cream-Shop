from django.test import TestCase

from ...forms import RegisterUserForm
from ...models import UserProfile
from .utils.abstract_tests import AbstractCharFieldTest


class RegisterUserFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        UserProfile.objects.create_user(username='existingusername', email='existingemail@mail.ru')

    def setUp(self) -> None:
        self.form_data = {
            'first_name': 'FirstName',
            'last_name': 'LastName',
            'username': 'itsmyusername',
            'email': 'example@mail.ru',
            'password1': 'its a super hard password',
            'password2': 'its a super hard password',
        }


class RegisterUserFormObjectTest(RegisterUserFormTest):
    def test_object_meta(self):
        form = RegisterUserForm()
        expected_field_order = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        self.assertEqual(form.field_order, expected_field_order)
        self.assertEqual(form.Meta.fields, expected_field_order)
        self.assertEqual(form.Meta.model, UserProfile)


class RegisterUserFormValidTest(RegisterUserFormTest):
    def test_form_valid(self):
        form_data = self.form_data
        form = RegisterUserForm(data=form_data)
        self.assertTrue(form.is_valid())

        user = form.save()
        self.assertEqual(user.first_name, form_data['first_name'])
        self.assertEqual(user.last_name, form_data['last_name'])
        self.assertEqual(user.username, form_data['username'])
        self.assertEqual(user.email, form_data['email'])
        self.assertTrue(UserProfile.objects.filter(username=form_data['username']).exists())


class RegisterUserFormExitingTest(RegisterUserFormTest):
    def test_form_with_existing_username(self):
        form_data = self.form_data
        form_data['username'] = 'existingusername'
        form = RegisterUserForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertTrue('username' in form.errors)

    def test_form_with_existing_email(self):
        form_data = self.form_data
        form_data['email'] = 'existingemail@mail.ru'
        form = RegisterUserForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertTrue('email' in form.errors)


class RegisterUserFormFirstNameTest(AbstractCharFieldTest, RegisterUserFormTest):
    form = RegisterUserForm
    field_name = 'first_name'
    placeholder = 'Ваше имя'
    label = 'Имя'
    required = True
    incorrect_values = ['InvalidFirstName123', 'Пробелы нельзя', 'Анатолий""№1!', '', '232', '   ']


class RegisterUserFormLastNameTest(AbstractCharFieldTest, RegisterUserFormTest):
    form = RegisterUserForm
    field_name = 'last_name'
    placeholder = 'Ваша фамилия'
    label = 'Фамилия'
    required = True
    incorrect_values = ['InvalidFirstName123', 'Пробелы нельзя', 'Анатолий""№1!', '', '232', '   ']


class RegisterUserFormUsernameTest(AbstractCharFieldTest, RegisterUserFormTest):
    form = RegisterUserForm
    field_name = 'username'
    placeholder = 'Имя пользователя'
    label = 'Username'
    required = True
    incorrect_values = []


class RegisterUserFormEmailTest(AbstractCharFieldTest, RegisterUserFormTest):
    form = RegisterUserForm
    field_name = 'email'
    placeholder = 'Email'
    label = 'Email'
    required = True
    incorrect_values = ['invalid.email@com', 'user@.com', 'user@com.', 'user.email@com.', 'user@.com.', 'user.com@com',
                        'asdasfsaf', 'a@', '2322', '    ', '', '2323@some', '32@3@23', 'example@mail']


class RegisterUserFormPassword1Test(AbstractCharFieldTest, RegisterUserFormTest):
    form = RegisterUserForm
    field_name = 'password1'
    placeholder = 'Пароль'
    label = 'Пароль'
    required = True
    incorrect_values = []


class RegisterUserFormPassword2Test(AbstractCharFieldTest, RegisterUserFormTest):
    form = RegisterUserForm
    field_name = 'password2'
    placeholder = 'Повторите пароль'
    label = 'Повторите пароль'
    required = True
    incorrect_values = []
