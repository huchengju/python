import unittest
import requests
import json
from interface import global_chache
from tools.transfer import transfer_all
from interface.Account_Security.bind_GA_page import bind_GA
from interface.Account_Security.bind_phone_page import bind_phone
from interface.common.register import register_action
from interface.common.get_data_from_db import check_user_is_exited,delete_user,get_user_id_by_email
from config.circumstance_config import get_config
from interface.common.login import hmac_password, get_headers,check_bind_ga,login
from interface.personal_account import ga_auth


# Filename: A_sign_in_test.py
# author: yujie.li
class SignInTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = "bottest@example.com"
        email = check_user_is_exited(self.email)
        if email is None:
            register_action(self.email)
            bind_GA(self.email,login(self.email))
            userid = get_user_id_by_email(self.email)
            bind_phone(userid,86,1357924680,login(self.email))
            transfer_all(userid, 10000000)
        else:
            pass

    def setUp(self):
        config = get_config()
        self.url = "https://" + config.get("host") + "/v1/sign-in"
        self.headers = get_headers()

    def test_sign_in_success(self):
        """ email 正确， password 正确， 登录成功"""
        email = "bottest@example.com"
        password = hmac_password(email, b"Password01")
        secretKey = check_bind_ga(email)
        if secretKey is None:
            ga = ""
        else:
            ga = ga_auth.get_totp_token(secretKey)
        payload = {"email": email, "password": password, "ga": ga}
        response = requests.request("POST", self.url, headers=self.headers, data=json.dumps(payload))
        # response = login(email)
        self.assertEqual("success", response.json()['status'])
        self.assertIsNotNone(response.json()['data'])

    def test_login_email_incorrect_and_pw_correct(self):
        """ email不正确， password正确， 登录不成功"""

        email_error = "bottest_error@example.com"
        email = "bottest@example.com"
        password = hmac_password(email, b"Password01")
        secretKey = check_bind_ga(email)
        if secretKey is None:
            ga = ""
        else:
            ga = ga_auth.get_totp_token(secretKey)
        payload = {"email": email_error, "password": password, "ga": ga}
        # payload = {"email": email_error, "password": password, "ga": ga_auth.get_totp_token(scretKey)}
        response = requests.request("POST", self.url, headers=self.headers, data=json.dumps(payload))
        self.assertEqual(200, response.status_code)
        self.assertEqual("fail", response.json()['status'])
        self.assertEqual("USER_EMAIL_OR_PASSWORD_INVALID", response.json()['code'])

    def test_login_email_correct_and_pw_incorrect(self):
        """ email正确， password不正确， 登录不成功"""

        email = "bottest@example.com"
        password = hmac_password(email, b"Password01")
        secretKey = check_bind_ga(email)
        if secretKey is None:
            ga = ""
        else:
            ga = ga_auth.get_totp_token(secretKey)
        payload = {"email": email, "password": password+"error", "ga": ga}
        response = requests.request("POST", self.url, data=json.dumps(payload), headers=self.headers)

        self.assertEqual(200, response.status_code)
        self.assertEqual("fail", response.json()['status'])
        self.assertEqual("PARAMETER_INVALID", response.json()['code'])


    def test_login_email_incorrect_and_pw_incorrect(self):
        """ email不正确， password不正确， 登录不成功"""

        email_error = "bottest_error@example.com"
        email = "bottest@example.com"
        password = hmac_password(email, b"Password02")
        secretKey = check_bind_ga(email)
        if secretKey is None:
            ga = ""
        else:
            ga = ga_auth.get_totp_token(secretKey)
        payload = {"email": email_error, "password": password, "ga": ga}
        response = requests.request("POST", self.url, data=json.dumps(payload), headers=self.headers)

        self.assertEqual(200, response.status_code)
        self.assertEqual("fail", response.json()['status'])
        self.assertEqual("USER_EMAIL_OR_PASSWORD_INVALID", response.json()['code'])

    def tearDown(self):
        print("-----test sign in end------")


if __name__ == "__main__":
    unittest.main(verbosity=2)