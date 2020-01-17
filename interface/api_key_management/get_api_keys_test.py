import unittest
from interface.common.api_key_management import add_api_key,get_api_keys,delete_api_key


# Filename: get_api_keys_test.py
# author: yujie.li

class GetApiKeysTest(unittest.TestCase):
    """测试获取api_keys"""
    def setUp(self):
        self.email = "bottest@example.com"
        add_api_key(True, True, self.email)

    def test_get_api_keys_success(self):
        response = get_api_keys(self.email)
        self.assertEqual(200, response.status_code)
        self.assertEqual("success", response.json()["status"])

    def tearDown(self):
        print("-----test get api keys end------")
        delete_api_key(self.email)


if __name__ == "__main__":
    unittest.main(verbosity=2)
