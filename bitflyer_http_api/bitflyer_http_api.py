import requests

from .exceptions import ServerConnectionError
from .market import Market


class BitflyerHttpApi:

    def __init__(self):
        self.base_url = 'https://api.bitflyer.com/v1/'
        self.timeout = 5

    def __request(self, endpoint: str, method: str = 'GET', params=None):
        if method == 'GET':
            try:
                return requests.get(self.base_url + endpoint, params=params, timeout=self.timeout)
            except requests.ConnectionError:
                raise ServerConnectionError()

    def get_market_status(self):
        return self.__request("gethealth").json()

    def get_ticker(self, product_code: Market):
        endpoint = "ticker"
        payloads = {'product_code': product_code.value}
        return self.__request(endpoint, params=payloads).json()
