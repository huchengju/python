import unittest
import requests
from config.circumstance_config import get_config
from interface.common.login import login,get_headers


# Filename: market_prices_test.py
# author: yujie.li
class MarketPricesTest(unittest.TestCase):
    """测试获取prices数据"""
    def setUp(self):
        config = get_config()
        self.email = "bottest@example.com"
        self.mp_url = "https://" + config.get("host") + "/v1/market/prices"
        self.my_token = login(self.email)
        self.mp_headers = get_headers(self.my_token)

    def test_market_prices_success(self):
        """获取prices数据成功"""
        response = requests.request("GET", self.mp_url, headers=self.mp_headers)
        self.assertEqual(200, response.status_code)
        self.assertEqual("success", response.json()['status'])
        self.assertIsNotNone(response.json()['data'])

    def tearDown(self):
        print("--------market prices test end-------")


if __name__ == '__main__':
    unittest.main(verbosity=2)