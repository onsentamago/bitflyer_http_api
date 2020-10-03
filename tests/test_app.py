import pytest
import requests

from bitflyer_http_api import BitflyerHttpApi, Market, ServerConnectionError


def test_get_ticker(mocker):
    mocker.patch('requests.get')
    bybit_http_api = BitflyerHttpApi()
    bybit_http_api.get_ticker(Market.BTC_JPY)
    requests.get.assert_called_once_with('https://api.bitflyer.com/v1/ticker',
                                         params={'product_code': 'BTC_JPY'},
                                         timeout=5)


def test_raise_exception(mocker):
    mocker.patch('requests.get', side_effect=requests.ConnectionError)
    bybit_http_api = BitflyerHttpApi()
    with pytest.raises(ServerConnectionError) as excinfo:
        bybit_http_api.get_ticker(Market.BTC_JPY)
    assert excinfo.value.message == "Connection error occurred"


def test_make_timestamp_readable():
    assert BitflyerHttpApi.make_timestamp_readable('1600479960') == '2020-09-19 01:46:00'
    assert BitflyerHttpApi.make_timestamp_readable(1600479960) == '2020-09-19 01:46:00'
