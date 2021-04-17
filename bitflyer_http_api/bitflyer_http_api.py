from typing import Union

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
                if 'error_message' in result.keys():
                    raise BitflyerInternalError(result['error_message'])
                return result
            except requests.ConnectionError:
                raise ServerConnectionError()

    @staticmethod
    def get_market(symbol: str) -> Market:
        member: Market
        for name, member in Market.__members__.items():
            if member.value == symbol:
                return member
        raise ValueError

    def get_market_status(self) -> dict:
        endpoint = "gethealth"
        return self.__request(endpoint)

    def get_ticker(self, symbol: Union[Market, str]) -> dict:
        endpoint = "ticker"
        if isinstance(symbol, Market):
            payloads = {'product_code': symbol.value}
        else:
            payloads = {'product_code': BitflyerHttpApi.get_market(symbol).value}

        return self.__request(endpoint, params=payloads)
