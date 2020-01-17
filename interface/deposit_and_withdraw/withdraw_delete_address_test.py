import unittest
from interface.common.withdraw import withdraw_delete_address,withdraw_add_address


# Filename: withdraw_delete_address_test.py
# author: yujie.li
class WithdrawDeleteAddress(unittest.TestCase):
    """测试删除提现地址"""
    def setUp(self):
        self.currency = "LTC"
        self.address = "mwewY6WqmYuuQ9xvm9wr5ZP6PsrUPvFdPV"
        self.email = "bottest@example.com"
        withdraw_add_address(self.currency, self.address, self.email)

    def test_withdraw_delete_address_success(self):
        """删除提现地址成功"""
        response = withdraw_delete_address(self.currency, self.email)
        self.assertEqual(200, response.status_code)
        self.assertEqual("success", response.json()["status"])

    def tearDown(self):
        print("-----test withdraw delete address end ------ ")


if __name__ == "__main__":
    unittest.main(verbosity=2)