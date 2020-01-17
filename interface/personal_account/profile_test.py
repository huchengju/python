import unittest
import requests
from config.circumstance_config import get_config
from interface.common.login import login,get_headers


# Filename: profile_test.py
# author: yujie.li
class ProfileTest(unittest.TestCase):
    """测试获取用户个人基本信息"""

    def setUp(self):
        config = get_config()
        self.email = "bottest@example.com"
        self.profile_url = "https://" + config.get("host") + "/v1/json/user/profile"
        # self.my_token = login.login("lantian70703843@qq.com")
        self.my_token = login(self.email)
        self.profile_headers = get_headers(self.my_token)

    def test_get_profile_success(self):
        """获取用户个人基本信息成功"""
        response = requests.request("GET", self.profile_url, headers=self.profile_headers)
        self.assertEqual(200, response.status_code)
        self.assertEqual("success", response.json()['status'])

    def tearDown(self):
        print("----------------test profile end----------")


if __name__ == '__main__':
    unittest.main(verbosity=2)