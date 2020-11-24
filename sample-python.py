import hmac
import time
from requests import Request, Session, Response
from typing import Optional, Dict, Any

class MCS:

    def __init__(self, api_key='', api_secret='', is_testnet=False):

        self.api_key = api_key
        self.api_secret = api_secret

        self._session = Session()

        if is_testnet is True:
            self.base_url = 'https://api.testnet.mycoinstory.com'
        else:
            self.base_url = 'https://api.mycoinstory.com'

    ##############################################################################################
    #  request                                                                                   #
    ##############################################################################################
    def get(self, end_point: str, is_sign_request, params: Optional[Dict[str, Any]] = None) -> Any:
        method = 'GET'
        request = Request(method, self.base_url + end_point, params=params)
        return self._request(method, end_point, is_sign_request, params, request)

    def post(self, end_point: str, is_sign_request, params: Optional[Dict[str, Any]] = None) -> Any:
        method = 'POST'
        request = Request(method, self.base_url + end_point, json=params)
        return self._request(method, end_point, is_sign_request, params, request)

    def put(self, end_point: str, is_sign_request, params: Optional[Dict[str, Any]] = None) -> Any:
        method = 'PUT'
        request = Request(method, self.base_url + end_point, json=params)
        return self._request(method, end_point, is_sign_request, params, request)

    def delete(self, end_point: str, is_sign_request, params: Optional[Dict[str, Any]] = None) -> Any:
        method = 'DELETE'
        request = Request(method, self.base_url + end_point, json=params)
        return self._request(method, end_point, is_sign_request, params, request)

    def _request(self, method: str, end_point: str, is_sign_request, params, request) -> Any:
        if is_sign_request is True:
            request.headers = self._make_auth_header(method, end_point, request, params)

        response: Response = self._session.send(request.prepare())

        try:
            return response.json()
        except Exception as e:
            print('\nException !')
            print('e = ', e)
            print(response)
            return {}

    def _make_auth_header(self, method: str, end_point: str, request, params):
        prepared = request.prepare()

        str_timestamp = str(int(time.time() * 1000.0))  # milliseconds
        signature_payload = str_timestamp + method + end_point  # {timestamp+method+endpoint+body}

        if params is not None and len(params) > 0:

            if method == 'GET':
                str_path_url = str(prepared.path_url)
                question_index = str_path_url.find('?')
                signature_payload += str_path_url[question_index:]
            else:
                str_json = prepared.body.decode()
                str_json = str_json.replace(' ', '')
                signature_payload += str_json

        signature = hmac.new(bytes(self.api_secret, "utf-8"), bytes(signature_payload.encode("utf-8")),
                             'sha256').hexdigest()

        headers = {
            'X-MCS-ACCESS-KEY': self.api_key,
            'X-MCS-SIGNATURE': signature,
            'X-MCS-TIMESTAMP': str_timestamp,
            'Content-Type': 'application/json; charset=utf-8',
        }

        return headers

    ##############################################################################################
    #  public                                                                                    #
    ##############################################################################################
    def get_orderbook(self, params):  # Orderbook
        return exchange.get(end_point='/orderbook', is_sign_request=False, params=params)

    def get_contract(self, params):  # Instruments
        return exchange.get(end_point='/contract', is_sign_request=False, params=params)

    def get_tickers(self, params):  # Tickers
        return exchange.get(end_point='/tickers', is_sign_request=False, params=params)

    def get_klines(self, params):  # Kline/Candlestick Data
        return exchange.get(end_point='/klines', is_sign_request=False, params=params)

    def get_trades(self, params):  # Trades
        return exchange.get(end_point='/trades', is_sign_request=False, params=params)

    def get_funding_rates(self, params):  # Funding Rate History
        return exchange.get(end_point='/funding/history', is_sign_request=False, params=params)

    ##############################################################################################
    #  private                                                                                   #
    ##############################################################################################

    def get_wallet_balances(self, params):  # Get Wallet Balance
        return exchange.get(end_point='/wallet/balances', is_sign_request=True, params=params)

    def get_wallet_incomes(self, params):  # Get Income History
        return exchange.get(end_point='/wallet/incomes', is_sign_request=True, params=params)

    def get_position(self, params):  # Get Position Information
        return exchange.get(end_point='/position', is_sign_request=True, params=params)

    def set_leverage(self, params):  # Change Leverage
        return exchange.put(end_point='/position/leverage', is_sign_request=True, params=params)

    def get_tradeFee(self, params):  # Get Trade Fee
        return exchange.get(end_point='/tradeFee', is_sign_request=True, params=params)

    def get_order_fills(self, params):  # Query Order Status
        return exchange.get(end_point='/order/fills', is_sign_request=True, params=params)

    def get_order(self, params):  # Query Order Status
        return exchange.get(end_point='/order', is_sign_request=True, params=params)

    def get_order_all(self, params):  # Get All Open Orders
        return exchange.get(end_point='/order/all', is_sign_request=True, params=params)

    def place_order(self, params):  # Place Order
        return exchange.post(end_point='/order', is_sign_request=True, params=params)

    def cancel_order(self, params):  # Cancel Order
        return exchange.delete(end_point='/order', is_sign_request=True, params=params)

    def cancel_order_all(self, params):  # Cancel All Open Orders
        return exchange.delete(end_point='/order/all', is_sign_request=True, params=params)


if __name__ == '__main__':

    api_key = '<INPUT_YOUR_API_KEY>'
    api_secret = '<INPUT_YOUR_API_SECRET>'
    exchange = MCS(api_key=api_key, api_secret=api_secret, is_testnet=True)

    params = {'symbol': 'BTCUSDT', 'depth': 3}
    response = exchange.get_orderbook(params)

    # params = {'symbol': 'BTCUSDT'}
    # response = exchange.get_contract(params)

    # params = {'symbol': 'BTCUSDT', 'interval': '1h', 'limit': 5}
    # response = exchange.get_klines(params)

    # params = {'symbol': 'BTCUSDT', 'limit': 5}
    # response = exchange.get_funding_rates(params)

    # params = {'asset': 'BTC'}
    # response = exchange.get_wallet_balances(params)

    # params = {'asset': 'BTC', 'limit': 3}
    # response = exchange.get_wallet_incomes(params)

    # params = {'symbol': 'BTCUSDT'}
    # response = exchange.get_position(params)

    # params = {'symbol': 'BTCUSDT', 'leverage': 7}
    # response = exchange.set_leverage(params)

    # params = {'symbol': 'BTCUSDT'}
    # response = exchange.get_tradeFee(params)

    # params = {'symbol': 'BTCUSDT', 'limit': 3}
    # response = exchange.get_order_fills(params)

    # params = {'symbol': 'BTCUSDT', 'orderId': '6c9a2a53-86d8-4fb9-aa4b-2259cdc3756a'}
    # response = exchange.get_order(params)

    # params = {'symbol': 'BTCUSDT'}
    # response = exchange.get_order_all(params)

    # params = {'symbol': 'BTCUSDT', 'orderType': 'LIMIT', 'orderSide': 'BUY', 'orderPrice': '10000', 'orderQuantity': 10}
    # response = exchange.place_order(params)

    # params = {'symbol': 'BTCUSDT', 'orderId': '6c9a2a53-86d8-4fb9-aa4b-2259cdc3756a'}
    # response = exchange.cancel_order(params)

    # params = {'symbol': 'BTCUSDT'}
    # response = exchange.cancel_order_all(params)


    print('\nresponse =')
    print(response)
