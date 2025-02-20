class Urls:

    BASE_URL = 'https://stellarburgers.nomoreparties.site'
    USER_REGISTER = f'{BASE_URL}/api/auth/register'
    USER_LOGIN = f'{BASE_URL}/api/auth/login'
    USER_UPDATE = f'{BASE_URL}/api/auth/user'
    CREATE_ORDER = f'{BASE_URL}/api/orders'
    GET_USER_ORDERS = f'{BASE_URL}/api/orders'

    USER_DELETE = f'{BASE_URL}/api/auth/user'
    HEADERS = {'Content-Type': 'application/json'}