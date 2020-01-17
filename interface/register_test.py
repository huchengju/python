import requests
import unittest
import json
import time
from interface import global_chache
from config.circumstance_config import get_config
from interface.common import register
from interface.common.login import get_headers


# Filename: register_test.py
# author: yujie.li
class RegisterTest(unittest.TestCase):
    """测试register"""
    def setUp(self):
        config = get_config()
        self.url = "https://" + config.get("host") + "/v1/register"
        self.headers = get_headers()
        self.now_time = time.strftime("%Y-%m-%d_%H_%M_%S")

    def test_a_register_email_correct_vcode_incorrect(self):
        """email正确 , code不正确 ，注册失败"""
        time.sleep(5)
        email = "bot" + self.now_time + "@example.com"
        vcode = register.register_vcode(email)
        payload = {
            "email": str(email),
            "zone": "+08:00",
            "code": str(vcode)+"88"
        }
        response = requests.request("POST", self.url, data=json.dumps(payload), headers=self.headers)
        print(response.text)
        self.assertEqual("fail", response.json()['status'])
        self.assertEqual("REGISTRATION_ACTIVATION_INVALID", response.json()['code'])

    def test_b_register_email_incorrect_vcode_correct(self):
        """email不正确 , code正确  注册失败"""
        time.sleep(4)
        email = "bot" + self.now_time + "@example.com"
        vcode = register.register_vcode(email)
        payload = {
            "email": str(email)+"error",
            "zone": "+08:00",
            "code": str(vcode)
        }
        response = requests.request("POST", self.url, data=json.dumps(payload), headers=self.headers)
        self.assertEqual("fail", response.json()['status'])
        self.assertEqual("REGISTRATION_ACTIVATION_INVALID", response.json()['code'])

    def test_c_register_email_correct_vcode_null(self):
        """email正确 , code为空 , 注册失败"""
        time.sleep(2)
        email = "bot" + self.now_time + "@example.com"
        vcode = register.register_vcode(email)
        payload = {
            "email": str(email),
            "zone": "+08:00",
            "code": ""
        }
        response = requests.request("POST", self.url, data=json.dumps(payload), headers=self.headers)
        self.assertEqual("fail", response.json()['status'])
        self.assertEqual("REGISTRATION_ACTIVATION_INVALID", response.json()['code'])

    def test_d_register_success(self):
        """email正确， vcode正确 ，注册成功"""
        email = "bot" + self.now_time + "@example.com"
        vcode = register.register_vcode(email)
        payload = {
            "email": str(email),
            "zone": "+08:00",
            "code": vcode
        }
        response = requests.request("POST", self.url, data=json.dumps(payload), headers=self.headers)
        self.assertEqual("success", response.json()['status'])

    def tearDown(self):

        print("----------test vcode reigster end--------------")


if __name__ == "__main__":
    unittest.main(verbosity=2)