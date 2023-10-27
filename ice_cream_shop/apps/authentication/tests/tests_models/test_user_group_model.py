from django.test import TestCase

from apps.authentication.models import UserGroup


class UserGroupTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        UserGroup.objects.create(name='Какая-то группа')

    def setUp(self) -> None:
        self.group = UserGroup.objects.get(pk=1)


class UserGroupObjectTest(UserGroupTest):
    def test_object_name_is_name(self):
        expected_object_name = self.group.name
        self.assertEqual(expected_object_name, str(self.group))

    def test_object_verbose_name(self):
        expected_verbose_name = self.group._meta.verbose_name
        self.assertEqual(expected_verbose_name, 'Группа')

    def test_object_verbose_name_plural(self):
        expected_verbose_name_plural = self.group._meta.verbose_name_plural
        self.assertEqual(expected_verbose_name_plural, 'Группы')


class UserGroupNameTest(UserGroupTest):
    def test_name_label(self):
        field_label = self.group._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'Имя')

    def test_name_max_length(self):
        max_length = self.group._meta.get_field('name').max_length
        self.assertEqual(max_length, 80)

    def test_name_unique(self):
        is_unique = self.group._meta.get_field('name').unique
        self.assertEqual(is_unique, True)


class UserGroupPermissionsTest(UserGroupTest):
    def test_permissions_label(self):
        field_label = self.group._meta.get_field('permissions').verbose_name
        self.assertEqual(field_label, 'Права')

    def test_permissions_related_model_name(self):
        related_model = self.group._meta.get_field('permissions').related_model
        self.assertEqual(related_model.__name__, 'Permission')

    def test_permissions_blank(self):
        is_blank = self.group._meta.get_field('permissions').blank
        self.assertEqual(is_blank, True)
