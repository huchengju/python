import unittest
import requests
from config.circumstance_config import get_config
from interface.common.login import login


# Filename: internal_send_phone_code.py
# author: yujie.li
class WithdrawSendPhoneCodeTest(unittest.TestCase):
    """内部提现发送手机验证码"""
    def setUp(self):
        config = get_config()
        self.email = "bottest@example.com"
        self.internal_url = "https://" + config.get("host") + "/v1/user/withdraw/send-phone-code?type=internal"
        self.my_token = login(self.email)
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": self.my_token,
        }

    def test_get_withdraw_send_phone_code_success(self):
        response = requests.request("GET", self.internal_url, headers=self.headers)
        self.assertEqual(200, response.status_code)
        self.assertEqual("success", response.json()["status"])

    def tearDown(self):
        print("--------test get internal send phone code end --------")


if __name__ == "__main__":
    unittest.main(verbosity=2)
