import logging

from bitflyer_http_api import BitflyerHttpApi, Market

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    bitflyer_http_api = BitflyerHttpApi()
    result = bitflyer_http_api.get_ticker(Market.BTC_JPY)
    logging.debug(result)
