import unittest
from interface.common.api_key_management import delete_api_key, add_api_key


# Filename: delete_api_key_test.py
# author: yujie.li
class DeleteApiKeyTest(unittest.TestCase):
    """测试删除api_key"""
    def setUp(self):
        self.email = "bottest@example.com"
        add_api_key(True, True, self.email)


    def test_delete_api_key_success(self):
        response = delete_api_key(self.email)
        self.assertEqual(200, response.status_code)
        self.assertEqual("success", response.json()["status"])

    def tearDown(self):
        print("-----test delete api key end ------ ")


if __name__ == "__main_":
    unittest.main(verbosity=2)