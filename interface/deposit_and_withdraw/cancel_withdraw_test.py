import unittest
from interface.common.withdraw import withdraw_action,cancel_withdraw
from interface.common.get_data_from_db import get_withdraw_status_by_userid,get_user_id_by_email


# Filename: cancel_withdraw_test.py
# author: yujie.li
class CancelWithdrawTest(unittest.TestCase):
    """测试cancel withdraw """
    def setUp(self):
        self.amount = 1
        self.currency = "LTC"
        self.address = "mwewY6WqmYuuQ9xvm9wr5ZP6PsrUPvFdPV"
        self.email = "bottest@example.com"
        self.phone = 1357924680
        self.userid = get_user_id_by_email(self.email)
        withdraw_action(self.amount,self.currency,self.address, self.phone, self.email)

    def test_cancel_withdraw_success(self):
        """测试cance withdraw 成功"""
        response = cancel_withdraw(self.email)
        withdraw_status = get_withdraw_status_by_userid(self.userid)
        self.assertEqual(200, response.status_code)
        self.assertEqual("success", response.json()["status"])
        self.assertEqual("CANCELLED", withdraw_status)

    def tearDown(self):
        print("-------test cancel withdraw end ------")


if __name__ == "__main__":
    unittest.main(verbosity=2)