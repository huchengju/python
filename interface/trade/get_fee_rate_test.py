import unittest
import requests
from config.circumstance_config import get_config
from interface.common.login import login, get_headers


# Filename: get_fee_rate_test.py
# author: yujie.li
class GetFeeRateTest(unittest.TestCase):
    """测试获取symbol的当前 fee rate"""
    def setUp(self):
        config = get_config()
        self.email = "bottest@example.com"
        self.url = "https://" + config.get("host") + "/v1/trade/getFeeRate?symbol=BTC_USDT"
        self.my_token = login(self.email)
        self.headers = get_headers(self.my_token)

    def test_get_fee_rate_success(self):
        """获取当前fee rate 成功"""
        response = requests.request("GET", self.url, headers=self.headers)
        self.assertEqual(200, response.status_code)
        self.assertEqual("success", response.json()['status'])
        self.assertIsNotNone(response.json()['data'])

    def tearDown(self):
        print("----------test get fee rate end ---------")


if __name__ == "__main__":
    unittest.main(verbosity=2)