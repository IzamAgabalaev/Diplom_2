import allure
from conftest import *
from data import DataUser, Messages


class TestLogin:
    @allure.title('Авторизация с валидными данными')
    def test_login_user_success(self, login_user, create_new_user_and_delete):
        access_token = login_user
        payload_cred, _ = create_new_user_and_delete
        response = requests.post(Urls.USER_LOGIN, data={
            'email': payload_cred['email'],
            'password': payload_cred['password']
        })
        response_body = response.json()
        assert access_token is not None
        assert response.status_code == 200
        assert response_body['success'] is True
        assert 'accessToken' in response_body
        assert 'refreshToken' in response_body
        assert 'user' in response_body
        assert response_body['user']['email'] == payload_cred['email']
        assert response_body['user']['name'] == payload_cred['name']

    @allure.title('Авторизация с незарегестрированным email')
    def test_login_email_invalid(self):
        payload = {
            'email': create_random_email(),
            'password': DataUser.PASSWORD,
        }
        response = requests.post(Urls.USER_LOGIN, data=payload)
        assert response.status_code == 401
        assert response.json()['success'] is False
        assert response.json()["message"] == Messages.ERROR_MESSAGES['invalid_data']

    @allure.title('Авторизация с невалидным паролем')
    def test_login_invalid_password(self):
        payload = {
            'email': DataUser.EMAIL,
            'password': create_random_password(),
        }
        response = requests.post(Urls.USER_LOGIN, data=payload)
        assert response.status_code == 401
        assert response.json()['success'] is False
        assert response.json()["message"] == Messages.ERROR_MESSAGES['invalid_data']

