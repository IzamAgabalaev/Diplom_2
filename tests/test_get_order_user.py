import allure
import requests
from conftest import *
from data import Messages
from urls import Urls

class TestGetOrderUser:

    @allure.title('Получение заказа авторизованного пользователя')
    def test_get_orders_authenticated_user_success(self, create_user_and_order_and_delete):
        headers = {'Authorization': create_user_and_order_and_delete[0]}
        response = requests.get(Urls.GET_USER_ORDERS, headers=headers)
        r = response.json()
        assert response.status_code == 200
        assert r['success'] is True
        assert 'orders' in r.keys()
        assert 'total' in r.keys()
        assert 'totalToday' in r.keys()

    @allure.title('Получение заказа неавторизованного пользователя')
    def test_get_orders_unauthenticated_user_success(self):
        response = requests.get(Urls.GET_USER_ORDERS, headers=Urls.HEADERS)
        assert response.status_code == 401
        assert response.json()['success'] is False
        assert response.json()['message'] == Messages.ERROR_MESSAGES['not_authorized']

