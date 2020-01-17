import unittest
from interface.common.index_page import add_symobl_option,remove_symbol_option


# Filename: add_symbol_option_test.py
# author: yujie.li
class AddSymbolOptionTest(unittest.TestCase):
    """测试add symbol option"""
    def setUp(self):
        self.symbol = "LTC_USDT"
        self.email = "bottest@example.com"

    def test_add_symbol_option_success(self):
        """add symbol option 成功"""
        response = add_symobl_option(self.symbol, self.email)
        self.assertEqual(200, response.status_code)
        self.assertEqual("success", response.json()["status"])

    def tearDown(self):
        print("------test add symbol option end -----")
        remove_symbol_option(self.symbol, self.email)


if __name__ == "__main__":
    unittest.main(verbosity=2)


