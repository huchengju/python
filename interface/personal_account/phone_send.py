from config.circumstance_config import get_config
from interface.common.login import login
import unittest
import requests
import json


# Filename: phone_send.py
# author: yujie.li
class TEST(unittest.TestCase):

    def test_phone(self):
        config = get_config()
        url = "https://"+ config.get("host") +"/v1/user/phone/sendMessage"
        token = login()
        headers={
            'Content-Type': 'application/json',
            'Authorization': token,
        }
        payload = {"phoneNumber": "13190000001","country": "86"}
        response = requests.request("POST",url, data=json.dumps(payload),headers=headers)
        print(response.text)