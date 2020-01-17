import unittest
from interface.common import withdraw


# Filename: withdraw_get_phone_code_test.py
# author: yujie.li

class WithdrawGetPhoneCode(unittest.TestCase):
    """测试提现获取 phone code"""
    def setUp(self):
        self.phone = 1357924680
        self.email = "bottest@example.com"

    def test_withdraw_get_phone_code_success(self):
        """提现获取phone code成功"""
        phone_code = withdraw.withdraw_get_phone_code(self.phone, self.email)
        print(phone_code)
        self.assertIsNotNone(phone_code)

    def tearDown(self):
        print("-----test withdraw get phone code end ------ ")


if __name__ == "__main__":
    unittest.main(verbosity=2)