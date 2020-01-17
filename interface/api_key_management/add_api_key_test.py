import unittest
from interface.common.api_key_management import add_api_key,delete_api_key


# Filename: add_api_key_test.py
# author: yujie.li

class AddApiKeyTest(unittest.TestCase):
    """测试获取api_keys"""
    def setUp(self):
        self.canTrade = True
        self.canWithdraw = True
        self.email = "bottest@example.com"

    def test_add_api_key_success(self):
        response = add_api_key(self.canTrade, self.canWithdraw,self.email)
        self.assertEqual(200, response.status_code)
        self.assertEqual("success", response.json()["status"])

    def tearDown(self):
        print("-----test add api key end------")
        delete_api_key(self.email)


if __name__ == "__main__":
    unittest.main(verbosity=2)
