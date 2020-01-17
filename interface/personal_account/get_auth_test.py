import unittest
import requests
from config.circumstance_config import get_config
from interface.common.login import login,get_headers


# Filename: get_auth_test.py
# author: yujie.li
class GetAuthTest(unittest.TestCase):
    """getAuth测试"""
    def setUp(self):
        config = get_config()
        self.email = "bottest@example.com"
        self.url = "https://" + config.get("host") + "/v1/google/user/security/getAuth"
        self.my_token = login(self.email)
        self.headers = get_headers(self.my_token)

    def test_get_auth_success(self):
        """测试 get auth 成功"""
        response = requests.request("GET", self.url, headers=self.headers)
        print(response.text)
        self.assertEqual(200, response.status_code)
        self.assertEqual("success", response.json()['status'])

    def tearDown(self):
        print("-----test get auth end -------")


if __name__ == "__main__":
    unittest.main(verbosity=2)