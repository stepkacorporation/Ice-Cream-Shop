from django.test import TestCase

from apps.authentication.models import UserProfile


class UserProfileTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        UserProfile.objects.create(
            first_name='FirstName',
            last_name='LastName',
            password='Password',
            email='example@mail.org',
        )

    def setUp(self) -> None:
        self.user = UserProfile.objects.get(pk=1)


class UserProfileObjectTest(UserProfileTest):
    def test_object_name_is_username(self):
        expected_object_name = self.user.username
        self.assertEqual(expected_object_name, str(self.user))

    def test_object_verbose_name(self):
        expected_verbose_name = self.user._meta.verbose_name
        self.assertEqual(expected_verbose_name, 'пользователь')

    def test_object_verbose_name_plural(self):
        expected_verbose_name_plural = self.user._meta.verbose_name_plural
        self.assertEqual(expected_verbose_name_plural, 'пользователи')


class UserProfileEmailTest(UserProfileTest):
    def test_email_label(self):
        field_label = self.user._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email')

    def test_email_is_unique(self):
        is_unique = self.user._meta.get_field('email').unique
        self.assertEqual(is_unique, True)


class UserProfileUserGroupsTest(UserProfileTest):
    def test_user_groups_label(self):
        field_label = self.user._meta.get_field('user_groups').verbose_name
        self.assertEqual(field_label, 'Группы')

    def test_user_groups_related_model_name(self):
        related_model = self.user._meta.get_field('user_groups').related_model
        self.assertEqual(related_model.__name__, 'UserGroup')

    def test_user_groups_blank(self):
        is_blank = self.user._meta.get_field('user_groups').blank
        self.assertEqual(is_blank, True)


class UserProfilePointsTest(UserProfileTest):
    def test_points_label(self):
        field_label = self.user._meta.get_field('points').verbose_name
        self.assertEqual(field_label, 'Баллы')

    def test_points_default_value(self):
        default_value = self.user._meta.get_field('points').default
        self.assertEqual(default_value, 0)

    def test_points_blank(self):
        is_blank = self.user._meta.get_field('points').blank
        self.assertEqual(is_blank, True)


class UserProfileIsVerifiedTest(UserProfileTest):
    def test_is_verified_label(self):
        field_label = self.user._meta.get_field('email_is_verified').verbose_name
        self.assertEqual(field_label, 'Подтвержденный email')

    def test_is_verified_default_value(self):
        default_value = self.user._meta.get_field('email_is_verified').default
        self.assertEqual(default_value, False)

    def test_is_verified_blank(self):
        is_blank = self.user._meta.get_field('email_is_verified').blank
        self.assertEqual(is_blank, True)


class UserProfileEmailVerificationTokenTest(UserProfileTest):
    def test_email_verification_token_max_length(self):
        max_length = self.user._meta.get_field('email_verification_token').max_length
        self.assertEqual(max_length, 255)

    def test_email_verification_token_label(self):
        field_label = self.user._meta.get_field('email_verification_token').verbose_name
        self.assertEqual(field_label, 'Email-токен')

    def test_email_verification_token_blank(self):
        is_blank = self.user._meta.get_field('email_verification_token').blank
        self.assertEqual(is_blank, True)


class UserProfileLastEmailVerificationRequestTest(UserProfileTest):
    def test_last_email_verification_request_label(self):
        field_label = self.user._meta.get_field('last_email_verification_request').verbose_name
        self.assertEqual(field_label, 'Дата последней отправки email пользователю')

    def test_last_email_verification_request_blank(self):
        is_blank = self.user._meta.get_field('last_email_verification_request').blank
        self.assertEqual(is_blank, True)

    def test_last_email_verification_request_null(self):
        is_null = self.user._meta.get_field('last_email_verification_request').null
        self.assertEqual(is_null, True)