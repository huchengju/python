import unittest
from interface.common.withdraw import get_fex


class GetFexTest(unittest.TestCase):
    """测试获取fex"""
    def setUp(self):
        self.fromBase = "BTC"
        self.toBase = "USDT"

    def test_get_fex_success(self):
        """测试获取fex成功"""
        response = get_fex(self.fromBase, self.toBase)
        self.assertEqual(200, response.status_code)
        self.assertEqual("success", response.json()["status"])

    def tearDown(self):
        print("------test ge fex success------")


if __name__ == "__main__":
    unittest.main(verbosity=2)