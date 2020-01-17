import unittest
from interface.common.withdraw import get_day_amount


# Filename: get_day_amount_test.py
# author: yujie.li
class GetDayAmountTest(unittest.TestCase):
    """测试获取当日已使用额度"""
    def setUp(self):
        self.email = "bottest@example.com"

    def test_get_day_amount(self):
        response = get_day_amount(self.email)
        self.assertEqual(200, response.status_code)
        self.assertEqual("success", response.json()["status"])

    def tearDown(self):
        print("-----test get day amount end -------")


if __name__ == "__main__":
    unittest.main(verbosity=2)
