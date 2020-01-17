import unittest
import requests
from config.circumstance_config import get_config
from interface.common.login import login,get_headers


# Filename: open_orders_test.py
# author: yujie.li
class OpenOrdersTest(unittest.TestCase):
    """测试获取open orders"""
    def setUp(self):
        config = get_config()
        self.email = "bottest@example.com"
        self.url = "https://" + config.get("host") + "/v1/trade/orders-by-pagination?pageNumber=1&pageSize=20&start=2019-06-18&end=2019-07-18&isFinalStatus=false&status=SUBMITTED%2CSEQUENCED%2CPARTIAL_FILLED&orderType=BUY_LIMIT%2CBUY_MARKET%2CSELL_LIMIT%2CSELL_MARKET"
        self.my_token = login(self.email)
        self.headers = get_headers(self.my_token)

    def test_get_open_orders(self):
        """获取open orders 成功"""
        response = requests.request("GET", self.url, headers=self.headers)
        self.assertEqual(200, response.status_code)
        self.assertEqual("success", response.json()['status'])

    def tearDown(self):
        print("------open orders test end------")


if __name__ == "__main__":
    unittest.main(verbosity=2)
