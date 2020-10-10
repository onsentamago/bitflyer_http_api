import logging

from bitflyer_http_api import BitflyerHttpApi

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    print(BitflyerHttpApi.get_previous_time(True))
