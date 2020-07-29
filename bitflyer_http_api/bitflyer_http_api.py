import requests

from .market import Market


class BitflyerHttpApi:

    def __init__(self):
        self.base_url = 'https://api.bitflyer.com/v1/'

    def __request(self, endpoint: str, method='GET', params=None):
        if method == 'GET':
            return requests.get(self.base_url + endpoint, params=params)

    def get_market_status(self):
        return self.__request("gethealth").json()

    def get_tiker(self, product_code: Market):
        payloads = {'product_code': product_code.value}
        return self.__request("ticker", params=payloads).json()
