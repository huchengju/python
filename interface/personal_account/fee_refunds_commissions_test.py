import unittest
import requests
from config.circumstance_config import get_config
from interface.common.login import login,get_headers


# Filename: fee_refunds_commissions_test.py
# author: yujie.li
class FeeRefundsCommissionsTest(unittest.TestCase):

    def setUp(self):
        config = get_config()
        self.email = "bottest@example.com"
        self.url = "https://" + config.get("host") + "/v1/feeRefunds/commissions"
        self.my_token = login(self.email)
        self.headers = get_headers(self.my_token)

    def test_fee_refunds_commissions(self):
        response = requests.request("GET", self.url, headers=self.headers)
        self.assertEqual(200, response.status_code)
        self.assertEqual("success", response.json()['status'])

    def tearDown(self):
        print("--------test fee refunds commissions end -------")


if __name__ == "__main__":
    unittest.main(verbosity=2)