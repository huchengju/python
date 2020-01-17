import unittest
from interface.common.logout import logout


class LogoutTest(unittest.TestCase):
    """测试logout"""
    def setUp(self):
        self.email = "bottest@example.com"

    def test_logout_success(self):
        """测试logout 成功"""
        response = logout(self.email)
        self.assertEqual(200, response.status_code)
        self.assertEqual("success", response.json()["status"])

    def tearDown(self):
        print("------test logout success------")


if __name__ == "__main__":
    unittest.main(verbosity=2)

