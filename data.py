from helpers import create_random_email, create_random_username, create_random_password


class DataUser:
    EMAIL = 'izam.agabalaev@yandex.ru'
    PASSWORD = 'Qwerty12345!'
    NAME = 'Izam'

    data_with_empty_fields = [
        {'email': create_random_email(),
         'password': '',
         'name': create_random_username()},
        {'email': '',
         'password': create_random_password(),
         'name': create_random_username()},
        {'email': create_random_email(),
         'password': create_random_password(),
         'name': ''}
    ]

class DataIngredient:

    BURGER_ONE = ['61c0c5a71d1f82001bdaaa73', '61c0c5a71d1f82001bdaaa6c',
                '61c0c5a71d1f82001bdaaa76', '61c0c5a71d1f82001bdaaa79']

    BURGER_TWO = ['61c0c5a71d1f82001bdaaa74', '61c0c5a71d1f82001bdaaa6d',
                '61c0c5a71d1f82001bdaaa7a', '61c0c5a71d1f82001bdaaa6f']

    NO_VALID_HASH = '61c0c5a71d1f85328ffbbb4g'