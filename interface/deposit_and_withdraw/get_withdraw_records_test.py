import unittest
from interface.common.withdraw import get_withdraw_records


# Filename: get_withdraw_records_test.py
# author: yujie.li
class GetWithdrawRecordsTest(unittest.TestCase):
    """测试获取提现页面基本信息"""
    def setUp(self):
        self.currency = "LTC"
        self.email = "bottest@example.com"

    def test_get_withdraw_records_success(self):
        response = get_withdraw_records(self.currency, self.email)
        self.assertEqual(200, response.status_code)
        self.assertEqual("success", response.json()["status"])
        self.assertEqual(self.currency, response.json()["data"]["currency"])

    def tearDown(self):
        print("------test get withdraw records success")


if __name__ == "__main__":
    unittest.main(verbosity=2)
