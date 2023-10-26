from django.core.exceptions import ValidationError

import re
from string import ascii_lowercase


def username_validator(value):
    if any([not (i in ascii_lowercase) for i in value]):
        raise ValidationError(
            'Имя пользователя должно состоять только из букв латинского алфавита в нижнем регистре.' + '-' * 100
        )


def _string_validator(value, error_message):
    if not re.search(r'^[a-zA-Z а-яА-ЯёЁ]+$', value):
        raise ValidationError(error_message)


def first_name_validator(value):
    _string_validator(value, 'Имя должно состоять только из букв русского или латинского алфавита.')


def last_name_validator(value):
    _string_validator(value, 'Фамилия должна состоять только из букв русского или латинского алфавита.')