import allure
import requests
from conftest import create_new_user_and_delete
from data import Messages
from helpers import create_random_email, create_random_password, create_random_username
from urls import Urls


class TestUpdateUser:

    update_user_data = {
        'email': create_random_email(),
        'password': create_random_password(),
        'name': create_random_username()
    }

    @allure.title('Обновление данных пользователя')
    def test_update_user_success(self, create_new_user_and_delete):
        response = requests.patch(Urls.USER_UPDATE, headers={
            'Authorization': create_new_user_and_delete[1]['accessToken']}, data=TestUpdateUser.update_user_data)
        r = response.json()
        assert response.status_code == 200
        assert r['success'] is True
        assert r['user']['email'] == TestUpdateUser.update_user_data['email']
        assert r['user']['name'] == TestUpdateUser.update_user_data['name']

    @allure.title('Обновление данных пользователя при неавторизованном пользователе')
    def test_update_no_login_user(self):
        response = requests.patch(Urls.USER_UPDATE, headers=Urls.HEADERS)
        assert response.status_code == 401
        assert response.json()['success'] is False
        assert response.json()['message'] == Messages.ERROR_MESSAGES['not_authorized']

