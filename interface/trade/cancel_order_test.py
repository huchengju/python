import unittest
import time
import requests
import json
import random
from config.circumstance_config import get_config
from interface.common.login import login, get_headers


# Filename: cancel_order_test.py
# author: yujie.li
class CancelOrderTest(unittest.TestCase):
    """测试cancel order """
    def setUp(self):
        self.config = get_config()
        self.email = "bottest@example.com"
        self.create_order_url = "https://" + self.config.get("host") + "/v1/trade/orders"
        self.my_token = login(self.email)
        self.headers = get_headers(self.my_token)
        time.sleep(2)

    def create_order(self):
        self.amount = round(random.uniform(10, 12), 5)
        self.price = round(random.uniform(2, 3), 2)
        self.symbol = random.choice(['ETH_USDT', 'LTC_USDT'])
        self.trade_type = random.choice(['BUY_LIMIT', 'SELL_LIMIT'])
        if self.trade_type == "BUY_LIMIT":
            self.price = self.price + 1
        else:
            self.price = self.price - 1
        # self.payload = {"price": self.price, "amount": self.amount, "total": "230", "type": self.trade_type,"symbol": self.symbol}
        self.payload = {"price": self.price, "amount": self.amount, "total": str(self.price * self.amount), "type": self.trade_type,"symbol": self.symbol}
        response = requests.request("POST", self.create_order_url, data=json.dumps(self.payload), headers=self.headers)
        print(response.text)
        global id
        if response.json()['status'] == 'success':
            if response.json()['data'] is not None:
                id = response.json()['data']['id']
                return id
            else:
                print("data   error")
        else:
            print("create order error")

    def test_cancel_order_success(self):
        """cancel order success"""
        id = self.create_order()
        self.url = "https://" + self.config.get('host') + "/v1/trade/orders/" + str(id) + "/cancel"
        response = requests.request("POST", self.url, headers=self.headers)
        self.assertEqual(200, response.status_code)
        self.assertEqual('success', response.json()['status'])
        self.assertIsNotNone(response.json()['data'])

    def tearDown(self):
        print("-------test cancel order end ------")


if __name__ == "__main__":
    unittest.main(verbosity=2)
