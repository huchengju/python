import unittest
from interface.common.withdraw import withdraw_action,cancel_withdraw
from interface.common.get_data_from_db import get_withdraw_amount_by_userid,get_user_id_by_email


# Filename: withdraw_action_test.py
# author: yujie.li
class WithdrawActionTest(unittest.TestCase):
    """测试withdraw"""
    def setUp(self):
        self.amount = 1
        self.currency = "LTC"
        self.address = "mwewY6WqmYuuQ9xvm9wr5ZP6PsrUPvFdPV"
        self.email = "bottest@example.com"
        self.phone = 1357924680
        self.userid = get_user_id_by_email(self.email)

    def test_withdraw_action_success(self):
        """测试do withdraw success"""
        response = withdraw_action(self.amount, self.currency, self.address,self.phone, self.email)
        withdraw_amount = get_withdraw_amount_by_userid(self.userid)
        self.assertEqual(200, response.status_code)
        self.assertEqual("success", response.json()["status"])
        self.assertEqual(float(withdraw_amount), self.amount)

    def tearDown(self):
        print("------test withdraw action end-----------")
        cancel_withdraw(self.email)


if __name__ == "__main__":
    unittest.main(verbosity=2)
