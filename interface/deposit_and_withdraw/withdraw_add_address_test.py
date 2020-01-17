import unittest
from interface.common.withdraw import withdraw_add_address,withdraw_delete_address


# Filename: withdraw_add_address_test.py
# author: yujie.li
class WithdrawAddAddress(unittest.TestCase):
    """测试添加提现地址"""
    def setUp(self):
        self.currency = "LTC"
        self.address = "mwewY6WqmYuuQ9xvm9wr5ZP6PsrUPvFdPV"
        self.email = "bottest@example.com"

    def test_withdraw_add_address_success(self):
        """添加提现地址成功"""
        response = withdraw_add_address(self.currency, self.address, self.email)
        self.assertEqual(200, response.status_code)
        self.assertEqual("success", response.json()["status"])

    def tearDown(self):
        print("-----test withdraw add address end ------ ")
        withdraw_delete_address(self.currency,self.email)


if __name__ == "__main__":
    unittest.main(verbosity=2)