import unittest
from interface.common.withdraw import withdraw_get_email_code


# Filename: withdraw_get_email_code_test.py
# author: yujie.li

class WithdrawGetEmailCode(unittest.TestCase):
    """测试提现获取email code"""
    def setUp(self):
        self.email = "bottest@example.com"

    def test_withdraw_get_email_code_success(self):
        """测试提现获取email code 成功"""
        email_code = withdraw_get_email_code(self.email)
        print(email_code)
        self.assertIsNotNone(email_code)

    def tearDown(self):
        print("-----test withdraw get email code end ------ ")


if __name__ == "__main__":
    unittest.main(verbosity=2)