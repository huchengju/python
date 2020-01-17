import unittest
from interface.common.api_key_management import add_api_key,edit_api_key,delete_api_key

# Filename: edit_api_key_test.py
# author: yujie.li
class EditApiKeyTest(unittest.TestCase):
    """测试编辑api_key"""
    def setUp(self):
        self.canTrade = True
        self.canWithdraw = True
        self.email = "bottest@example.com"
        add_api_key(self.canTrade, self.canWithdraw, self.email)

    def test_edit_api_key_success(self):
        """测试编辑api_key成功"""
        response = edit_api_key(self.canTrade, self.canWithdraw, self.email)
        self.assertEqual(200, response.status_code)
        self.assertEqual("success", response.json()["status"])

    def tearDown(self):
        delete_api_key(self.email)
        print("------test edit api key end--------")


if __name__ == "__main__":
    unittest.main(verbosity=2)