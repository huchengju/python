import unittest
import time
import random
import requests
import json
from config.circumstance_config import get_config
from interface.common.login import login, get_headers


# Filename: create_order_test.py
# author: yujie.li
class CreateOrderTest(unittest.TestCase):
    """测试create order"""
    def setUp(self):
        config = get_config()
        self.email = "bottest@example.com"
        self.url = "https://" + config.get("host") + "/v1/trade/orders"
        self.my_token = login(self.email)
        time.sleep(2)
        self.headers = get_headers(self.my_token)
        self.amount = round(random.uniform(10, 12), 5)
        self.price = round(random.uniform(2, 3), 2)
        self.symbol = random.choice(['ETH_USDT', 'LTC_USDT'])
        self.trade_type = random.choice(['BUY_LIMIT', 'SELL_LIMIT'])
        if self.trade_type == "BUY_LIMIT":
            self.price = self.price + 1
        else:
            self.price = self.price - 1

    def test_create_orders_success(self):
        """create order success"""
        # payload = {"price":"6","amount":"5","total":"30.0000000","type":"BUY_LIMIT","symbol":"ETH_USDT"}
        payload = {"price": self.price, "amount": self.amount, "total": str(self.price * self.amount), "type": self.trade_type,"symbol": self.symbol}
        print(payload)
        response = requests.request("POST", self.url, data=json.dumps(payload), headers=self.headers)
        self.assertEqual(200, response.status_code)
        self.assertEqual("success", response.json()['status'])
        self.assertIsNotNone(response.json()['data'])

    def tearDown(self):
        print("-----test create orders end--------")


if __name__ == "__main__":
    unittest.main(verbosity=2)