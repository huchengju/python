import unittest
from interface.common.index_page import get_symbol_data

# Filename: get_symbol_data_test.py
# author: yujie.li
class GetSymbolDataTest(unittest.TestCase):
    """测试获取symbol data 数据"""
    def setUp(self):
        pass

    def test_get_symbol_data_success(self):
        """测试获取symbol data 数据成功"""
        response = get_symbol_data()
        print(response)
        self.assertEqual(200, response.status_code)
        self.assertEqual("success", response.json()["status"])

    def tearDown(self):
        print("----- test get symbol data success ------")


if __name__ == "__main__":
    unittest.main(verbosity=2)