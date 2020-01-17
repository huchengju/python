import unittest
import requests
import json
from config.circumstance_config import get_config
from interface.common.login import login, hmac_password, get_headers
from interface.personal_account import change_pass_get_email
from interface.common.get_data_from_db import check_user_is_exited
from interface.common.register import register_action


# Filename: change_password_test.py
# author: yujie.li
class ChangePasswordTest(unittest.TestCase):
    """测试change password"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = "bot02@example.com"
        email = check_user_is_exited(self.email)
        if email is None:
            register_action(self.email)
        else:
            pass

    def setUp(self):
        config = get_config()
        self.email = "bot02@example.com"
        self.url = "http://" + config.get("host") + "/v1/json/user/change-password"
        self.my_token = login(self.email)
        self.headers = get_headers(self.my_token)

    def test_change_password(self):
        change_pass_get_email.get_email(self.email)
        new_password = hmac_password(self.email, b"Password01")
        old_password = hmac_password(self.email, b"Password01")
        payload = {"newPassword":new_password,"oldPassword":old_password}
        response = requests.request("POST", self.url, data=json.dumps(payload), headers=self.headers)
        self.assertEqual(200, response.status_code)
        self.assertEqual("success", response.json()['status'])

    def tearDown(self):
        print("----- test change password end ------")


if __name__ == "__main__":
    unittest.main(verbosity=2)