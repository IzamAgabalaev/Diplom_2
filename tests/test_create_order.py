import allure
import pytest
import requests
from conftest import create_new_user_and_delete
from data import DataIngredient, Messages
from urls import Urls


class TestCreateOrder:
    @allure.title('Создание заказа авторизованным пользователем')
    @pytest.mark.parametrize('burger_ing', [DataIngredient.BURGER_ONE, DataIngredient.BURGER_TWO])
    def test_create_order_login_user(self, create_new_user_and_delete, burger_ing):
        headers = {'Authorization': create_new_user_and_delete[1]['accessToken']}
        payload = {'ingredients': [burger_ing]}
        response = requests.post(Urls.CREATE_ORDER, data=payload, headers=headers)
        r = response.json()
        assert response.status_code == 200
        assert r['success'] is True
        assert 'name' in r.keys()
        assert 'number' in r['order'].keys()

    @allure.title('Создание заказа неавторизованным пользователем')
    @pytest.mark.parametrize('burger_ing', [DataIngredient.BURGER_ONE, DataIngredient.BURGER_TWO])
    def test_create_order_dont_login_user(self, burger_ing):
        payload = {'ingredients': [burger_ing]}
        response = requests.post(Urls.CREATE_ORDER, data=payload)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title('Создание заказа авторизованным пользователем без ингредиентов')
    def test_create_order_login_user_no_ingredients(self, create_new_user_and_delete):
        headers = {'Authorization': create_new_user_and_delete[1]['accessToken']}
        payload = {'ingredients': []}
        response = requests.post(Urls.CREATE_ORDER, data=payload, headers=headers)
        assert response.status_code == 400
        assert response.json()['success'] is False
        assert response.json()['message'] == Messages.ERROR_MESSAGES['ingredient_id']

    @allure.title('Создание заказа неавторизованным пользователем без ингредиентов')
    def test_create_order_no_login_user_no_ingredients(self):
        payload = {'ingredients': []}
        response = requests.post(Urls.CREATE_ORDER, data=payload, headers=Urls.HEADERS)
        assert response.status_code == 400
        assert response.json()['success'] is False
        assert response.json()['message'] == Messages.ERROR_MESSAGES['ingredient_id']

    @allure.title('Создание заказа авторизованным пользователем c невалидным хэшом ингредиентов')
    def test_create_order_login_user_and_invalid_hash(self, create_new_user_and_delete):
        headers = {'Authorization': create_new_user_and_delete[1]['accessToken']}
        payload = {'ingredients': [DataIngredient.NO_VALID_HASH]}
        response = requests.post(Urls.CREATE_ORDER, data=payload, headers=headers)
        assert response.status_code == 500

