import unittest
import requests
from config.circumstance_config import get_config
from interface.common.login import login,get_headers


# Filename: trade_history_test.py
# author: yujie.li
class TradeHistoryTest(unittest.TestCase):
    """获取trade history"""
    def setUp(self):
        config = get_config()
        self.email = "bottest@example.com"
        self.url = "https://" + config.get("host") + "/v1/trade/matchDetails-by-pagination?pageNumber=1&pageSize=60&start=2019-06-18&end=2019-07-18&orderType=BUY_LIMIT%2CBUY_MARKET%2CSELL_LIMIT%2CSELL_MARKET"
        self.my_token = login(self.email)
        print(self.my_token)
        self.headers = get_headers(self.my_token)

    def test_get_trade_history_success(self):
        response = requests.request("GET", self.url, headers=self.headers)
        self.assertEqual(200, response.status_code)
        self.assertEqual("success", response.json()['status'])

    def tearDown(self):
        print("--------trade history end ---------")


if __name__ == "__main__":
    unittest.main(verbosity=2)
