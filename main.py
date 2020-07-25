from bitflyer_http_api import BitflyerHttpApi, Market

if __name__ == "__main__":
    bitflyer_http_api = BitflyerHttpApi()
    result = bitflyer_http_api.get_tiker(Market.BTC_JPY)
    print(result.json())
