import unittest
import requests
from config.circumstance_config import get_config
from interface.common.login import login,get_headers


# Filename: security_get_auth.py
# author: yujie.li
class SecurityGetAuthTest(unittest.TestCase):
    """测试security getAuth"""

    def setUp(self):
        config = get_config()
        self.email = "bottest@example.com"
        self.url = "https://" + config.get("host") + "/v1/google/user/security/getAuth"
        self.my_token = login(self.email)
        self.headers = get_headers(self.my_token)

    def test_security_get_auth_success(self):
        """测试security getAuth 成功"""
        response = requests.request("GET", self.url, headers=self.headers)
        self.assertEqual(200, response.status_code)
        self.assertEqual("success", response.json()['status'])

    def tearDown(self):
        print("-----------test security getAuth end ----------")


if __name__ == "__main__":
    unittest.main(verbosity=2)
