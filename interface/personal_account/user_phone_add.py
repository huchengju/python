import unittest
import requests
import json
from config.circumstance_config import get_config
from interface.common.login import login


# Filename: user_phone_add.py
# author: yujie.li
class UserPhoneAddTest(unittest.TestCase):
    """添加手机验证"""
    def setUp(self):
        config = get_config()
        self.email = "bottest@example.com"
        self.url = "https://" + config.get("host") + "/v1/user/phone/add"
        self.my_token = login(self.email)
        self.headers = {
            'contentType': 'application/json',
            'Authorization': self.my_token,
            'accept': "application/json",
        }

    def test_user_phone_add_test(self):
        payload = {"emailCode":"670562","phoneNumber":"13190000001","messageCode":"000796","country":"86"}