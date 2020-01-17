import unittest
from interface.common.index_page import add_symobl_option,remove_symbol_option


# Filename: remove_symbol_option_test.py
# author: yujie.li
class RemoveSymbolOptionTest(unittest.TestCase):
    """测试remove symbol option """

    def setUp(self):
        self.symbol = "LTC_USDT"
        self.email = "bottest@example.com"
        add_symobl_option(self.symbol, self.email)

    def test_remove_symbol_option_success(self):
        """测试 remove symbol option 成功"""
        response = remove_symbol_option(self.symbol, self.email)
        self.assertEqual(200, response.status_code)
        self.assertEqual("success", response.json()["status"])

    def tearDown(self):
        print("-----test remove symbol option end ----")


if __name__ == "__main__":
    unittest.main(verbosity=2)