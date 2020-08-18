import requests

from bitflyer_http_api import BitflyerHttpApi, Market


def test_get_ticker(mocker):
    mocker.patch('requests.get')
    bybit_http_api = BitflyerHttpApi()
    bybit_http_api.get_ticker(Market.BTC_JPY)
    requests.get.assert_called_once_with('https://api.bitflyer.com/v1/ticker',
                                         params={'product_code': 'BTC_JPY'})
