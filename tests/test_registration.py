import allure
import requests
from conftest import *
from data import DataUser

class TestRegistration:
    @allure.title('Регистрация с валидными данными')
    def test_registration_valid(self, create_new_user_and_delete):
        payload_cred, response_body = create_new_user_and_delete
        assert response_body.get('success') is True
        assert 'accessToken' in response_body.keys()
        assert 'refreshToken' in response_body.keys()
        assert response_body['user']['email'] == payload_cred['email']
        assert response_body['user']['name'] == payload_cred['name']

    @allure.title('Регистрация с путыми полями')
    @pytest.mark.parametrize('credentials', DataUser.data_with_empty_fields)
    def test_dont_use_one_input(self, credentials):
        response = requests.post(Urls.USER_REGISTER, data=credentials)
        assert response.status_code == 403
        response.json() == {'success': False, 'message': 'Email, password and name are required fields'}

    @allure.title('Регистрация с существующим email')
    def test_registration_existing_email(self):
        payload = {
            'email': DataUser.EMAIL,
            'password': create_random_password(),
            'name': create_random_username()
        }
        response = requests.post(Urls.USER_REGISTER, data=payload)
        assert response.status_code == 403
        assert response.json() == {'success': False, 'message': 'User already exists'}