import unittest
import requests
from config.circumstance_config import get_config
from interface.common.login import login,get_headers


# Filename: token_refresh_test.py
# author: yujie.li
class TokenRefreshTest(unittest.TestCase):
    """测试token refresh"""

    def setUp(self):
        config = get_config()
        self.email = "bottest@example.com"
        self.url = "https://" + config.get("host") + "/v1/token/refresh"
        self.my_token = login(self.email)
        self.headers = get_headers(self.my_token)

    def test_token_refresh_success(self):
        """测试token refresh 成功"""
        response = requests.request("POST", self.url, headers=self.headers)
        self.assertEqual(200, response.status_code)
        self.assertEqual("success", response.json()['status'])
        self.assertNotEqual(self.my_token, response.json()['data']['token'])
        print(response.json()['data']['token'])

    def tearDown(self):
        print("----------test token refresh end ---------")


if __name__ == "__main__":
    unittest.main(verbosity=2)