import logging

from bitflyer_http_api import BitflyerHttpApi, Market, ServerConnectionError, BitflyerInternalError

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    bitflyer_http_api = BitflyerHttpApi()
    try:
        result = bitflyer_http_api.get_ticker(Market.BTC_JPY)
        logging.debug(result)
    except ServerConnectionError:
        logging.warning('connection error occurred')
    except BitflyerInternalError:
        logging.warning('bitflyer internal error occurred')
