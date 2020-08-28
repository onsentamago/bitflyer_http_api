import requests

from .exceptions import ServerConnectionError, BitflyerInternalError
from .market import Market


class BitflyerHttpApi:

    def __init__(self):
        self.base_url = 'https://api.bitflyer.com/v1/'
        self.timeout = 5

    def __request(self, endpoint: str, method: str = 'GET', params: dict = None) -> dict:
        if method == 'GET':
            try:
                result: dict = requests.get(self.base_url + endpoint, params=params, timeout=self.timeout) \
                    .json()
                if 'status' in result.keys() and result['status'] < 0:
                    raise BitflyerInternalError(result['error_message'])
                return result
            except requests.ConnectionError:
                raise ServerConnectionError()

    def get_market_status(self) -> dict:
        endpoint = "gethealth"
        return self.__request(endpoint)

    def get_ticker(self, product_code: Market) -> dict:
        endpoint = "ticker"
        payloads = {'product_code': product_code.value}
        return self.__request(endpoint, params=payloads)
