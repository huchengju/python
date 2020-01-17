import unittest
import requests
from config.circumstance_config import get_config
from interface.common.login import login,get_headers


# Filename: user_account_test.py
# author: yujie.li
class UserAccountsTest(unittest.TestCase):
    """测试获取账户currency金额情况"""

    def setUp(self):
        config = get_config()
        self.email = "bottest@example.com"
        self.ua_url = "https://" + config.get("host") + "/v1/user/accounts"
        self.my_token = login(self.email)
        print(self.my_token)
        self.ua_headers = get_headers(self.my_token)

    def test_get_user_accounts_success(self):
        """获取账户currency金额成功"""
        response = requests.request("GET", self.ua_url, headers=self.ua_headers)
        # print(response.text)
        self.assertEqual(200, response.status_code)
        self.assertEqual("success", response.json()['status'])
        # print(response.json()['data'])
        self.assertIsNotNone(response.json()['data'])

    def tearDown(self):
        print("----------test user accounts end -------")


if __name__ == "__main__":
    unittest.main(verbosity=2)