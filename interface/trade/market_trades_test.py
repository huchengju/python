import unittest
import requests
from config.circumstance_config import get_config
from interface.common.login import login,get_headers


# Filename: market_trades_test.py
# author: yujie.li
class MarketTradesTest(unittest.TestCase):
    """测试获取market trades"""

    def setUp(self):
        config = get_config()
        self.email = "bottest@example.com"
        self.mt_url = "https://" + config.get("host") + "/v1/market/trades"
        self.my_token = login(self.email)
        self.mt_headers = get_headers(self.my_token)

    def test_market_trades_success(self):
        """获取market trades成功"""
        response = requests.request("GET", self.mt_url, headers=self.mt_headers)
        self.assertEqual(200, response.status_code)
        self.assertEqual("success", response.json()['status'])

    def tearDown(self):
        print('------test trades end-------------')


if __name__ == "__main__":
    unittest.main(verbosity=2)