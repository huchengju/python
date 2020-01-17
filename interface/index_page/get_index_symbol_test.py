import unittest
from interface.common.index_page import get_index_symbol

# Filename: get_index_symbo_test.py
# author: yujie.li
class GetIndexSymbolTest(unittest.TestCase):
    """测试获取index symbol数据"""
    def setUp(self):
        pass

    def test_get_index_symbol_success(self):
        """测试获取index symbol 数据成功"""
        response = get_index_symbol()
        self.assertEqual(200, response.status_code)
        self.assertEqual("success", response.json()["status"])
        self.assertIsNotNone(response.json()["data"])

    def tearDown(self):
        print("-------test get index symbol end --------")


if __name__ == "__main__":
    unittest.main(verbosity=2)