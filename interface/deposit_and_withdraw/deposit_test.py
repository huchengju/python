import unittest
from interface.common.deposit import get_deposit_address_and_record,get_deposit_record


# Filename: deposit_test.py
# author: yujie.li
class GetDepositAddressAndRecord(unittest.TestCase):
    """测试获取用户单个币种的基本充值信息"""
    def setUp(self):
        self.currency = "LTC"
        self.email = "bottest@example.com"

    def test_get_deposit_address_and_record_success(self):
        response = get_deposit_address_and_record(self.currency, self.email)
        self.assertEqual(200, response.status_code)
        self.assertEqual("success", response.json()["status"])
        self.assertEqual("LTC", response.json()["data"]["currency"])

    def tearDown(self):
        print("-----test get deposit address and record end------")


class GetDepositRecord(unittest.TestCase):
    def setUp(self):
        self.currency = "LTC"
        self.email = "bottest@example.com"

    def test_get_deposit_record_success(self):
        response = get_deposit_record(self.currency, self.email)
        self.assertEqual(200, response.status_code)
        self.assertEqual("success", response.json()["status"])
        self.assertIsNotNone(response.json()["data"])

    def tearDown(self):
        print("------test get deposit record end------")
#

if __name__ == "main":
    unittest.main(verbosity=2)


