import unittest
import requests
from config.circumstance_config import get_config
from interface.common.login import login,get_headers


# Filename: order_history_test.py
# author: yujie.li
class OrderHistoryTest(unittest.TestCase):
    """测试获取order history"""
    def setUp(self):
        config = get_config()
        self.email = "bottest@example.com"
        self.url = "https://" + config.get("host") + "/v1/trade/orders-by-pagination?pageNumber=1&pageSize=60&start=2019-06-18&end=2019-07-18&isFinalStatus=true&status=FULLY_FILLED%2CPARTIAL_CANCELLED%2CFULLY_CANCELLED&orderType=BUY_LIMIT%2CBUY_MARKET%2CSELL_LIMIT%2CSELL_MARKET"
        self.my_token = login(self.email)
        self.headers = get_headers(self.my_token)

    def test_get_order_history_success(self):
        """获取order history 成功"""
        response = requests.request("GET", self.url, headers=self.headers)
        self.assertEqual(200, response.status_code)
        self.assertEqual("success", response.json()['status'])

    def tearDown(self):
        print("----------order history test end------------")


if __name__ == "__main__":
    unittest.main(verbosity=2)