import unittest
import requests
from config.circumstance_config import get_config
from interface.common.login import login,get_headers


# Filename: fee_refunds_info_test.py
# author: yujie.li
class FeeRefundsInfoTest(unittest.TestCase):

    def setUp(self):
        config = get_config()
        self.email = "bottest@example.com"
        self.url = "https://" + config.get("host") + "/v1/feeRefunds/info"
        self.my_token = login(self.email)
        self.headers = get_headers(self.my_token)

    def test_fee_refunds_info(self):
        response = requests.request("GET", self.url, headers=self.headers)
        self.assertEqual(200, response.status_code)
        self.assertEqual("success", response.json()['status'])
        self.assertIsNotNone(response.json()['data']['inviteCode'])

    def tearDown(self):
        print("--------test fee refunds info end -------")


if __name__ == "__main__":
    unittest.main(verbosity=2)