import pytest
import requests

from data import DataIngredient
from helpers import create_random_email, create_random_password, create_random_username
from urls import Urls


@pytest.fixture
def create_new_user_and_delete():
    payload_cred = {
        'email': create_random_email(),
        'password': create_random_password(),
        'name': create_random_username()
    }
    response = requests.post(Urls.USER_REGISTER, data=payload_cred)
    response_body = response.json()

    yield payload_cred, response_body

    access_token = response_body['accessToken']
    requests.delete(Urls.USER_DELETE, headers={'Authorization': access_token})

@pytest.fixture
def create_user_and_order_and_delete(create_new_user_and_delete):
    access_token = create_new_user_and_delete[1]['accessToken']
    headers = {'Authorization': access_token}
    payload = {'ingredients': [DataIngredient.BURGER_TWO]}
    response_body = requests.post(Urls.CREATE_ORDER, data=payload, headers=headers)

    yield access_token, response_body

    requests.delete(Urls.USER_DELETE, headers={'Authorization': access_token})

@pytest.fixture()
def login_user(create_new_user_and_delete):
    payload_cred, _ = create_new_user_and_delete
    response = requests.post(Urls.USER_LOGIN, data={
        'email': payload_cred['email'],
        'password': payload_cred['password']
    })
    response_body = response.json()

    yield response_body['accessToken']



