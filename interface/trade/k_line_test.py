import unittest
import requests
from config.circumstance_config import get_config
from interface.common.login import login, get_headers


# Filename: k_line_test.py
# author: yujie.li

class K1MinTest(unittest.TestCase):
    """测试1 minute k 线图"""
    def setUp(self):
        config = get_config()
        self.email = "bottest@example.com"
        self.url = "https://" + config.get("host") + "/v1/market/bars/ETH_USDT/K_1_MIN"
        self.my_token = login(self.email)
        self.headers = get_headers(self.my_token)

    def test_get_k_1_min(self):
        """获取1 minute k线图成功"""
        response = requests.request("GET", self.url, headers=self.headers)
        self.assertEqual(200, response.status_code)
        self.assertEqual("success", response.json()['status'])
        self.assertIsNotNone(response.json()['data'])

    def tearDown(self):
        print("--------test k 1 minutes end -----------")


class K5MinTest(unittest.TestCase):
    """测试5 minutes k线图"""
    def setUp(self):
        config = get_config()
        self.email = "bottest@example.com"
        self.url = "https://" + config.get("host") + "/v1/market/bars/ETH_USDT/K_5_MIN"
        self.my_token = login(self.email)
        self.headers = get_headers(self.my_token)

    def test_get_k_5_min(self):
        """获取5 minutes k线图成功"""
        response = requests.request("GET", self.url, headers=self.headers)
        self.assertEqual(200, response.status_code)
        self.assertEqual("success", response.json()['status'])
        self.assertIsNotNone(response.json()['data'])

    def tearDown(self):
        print("--------test k 5 minutes end ---------")


class K15MinTest(unittest.TestCase):
    """测试15 minutes k线图"""

    def setUp(self):
        config = get_config()
        self.email = "bottest@example.com"
        self.url = "https://" + config.get("host") + "/v1/market/bars/ETH_USDT/K_15_MIN"
        self.my_token = login(self.email)
        self.headers = get_headers(self.my_token)

    def test_get_k_15_min(self):
        """测试获取15 minutes K线图成功"""
        response = requests.request("GET", self.url, headers=self.headers)
        self.assertEqual(200, response.status_code)
        self.assertEqual("success", response.json()['status'])
        self.assertIsNotNone(response.json()['data'])

    def tearDown(self):
        print("-------- test k 30 minutes end --------")


class K30MinTest(unittest.TestCase):
    """测试30 minutes k线图"""
    def setUp(self):
        config = get_config()
        self.email = "bottest@example.com"
        self.url = "https://" + config.get("host") + "/v1/market/bars/ETH_USDT/K_30_MIN"
        self.my_token = login(self.email)
        self.headers = get_headers(self.my_token)

    def test_get_k_30_min(self):
        """获取30 minutes k线图成功"""
        response = requests.request("GET", self.url, headers=self.headers)
        self.assertEqual(200, response.status_code)
        self.assertEqual("success", response.json()['status'])
        self.assertIsNotNone(response.json()['data'])

    def tearDown(self):
        print("--------test k 30 minutes end --------")


class K1HourTest(unittest.TestCase):
    """测试1小时k线图"""
    def setUp(self):
        config = get_config()
        self.email = "bottest@example.com"
        self.k_one_url = "https://" + config.get("host") + "/v1/market/bars/ETH_USDT/K_1_HOUR"
        self.my_token = login(self.email)
        self.headers = get_headers(self.my_token)

    def test_get_k_1_hour_success(self):
        """获取1小时k线图成功"""
        response = requests.request("GET", self.k_one_url, headers=self.headers)
        self.assertEqual(200, response.status_code)
        self.assertEqual("success", response.json()['status'])
        self.assertIsNotNone(response.json()['data'])

    def tearDown(self):
        print("---------test k one hour end------------")


class K4HoursTest(unittest.TestCase):
    """测试4 hours k 线图"""

    def setUp(self):
        config = get_config()
        self.email = "bottest@example.com"
        self.url = "https://" + config.get("host") + "/v1/market/bars/ETH_USDT/K_4_HOUR"
        self.my_token = login(self.email)
        self.headers = get_headers(self.my_token)

    def test_get_k_4_hours(self):
        """测试获取4 hours k线图成功"""
        response = requests.request("GET", self.url, headers=self.headers)
        self.assertEqual(200, response.status_code)
        self.assertEqual("success", response.json()['status'])
        self.assertIsNotNone(response.json()['data'])

    def tearDown(self):
        print("--------test k 4 hours end -----------")


class K8HoursTest(unittest.TestCase):
    """测试8 hours k 线图"""

    def setUp(self):
        config = get_config()
        self.email = "bottest@example.com"
        self.url = "https://" + config.get("host") + "/v1/market/bars/ETH_USDT/K_8_HOUR"
        self.my_token = login(self.email)
        self.headers = get_headers(self.my_token)

    def test_get_k_8_hours(self):
        """测试获取8 hours k 线图成功"""
        response = requests.request("GET", self.url, headers=self.headers)
        self.assertEqual(200, response.status_code)
        self.assertEqual("success", response.json()['status'])
        self.assertIsNotNone(response.json()['data'])

    def tearDown(self):
        print("--------test k 8 hours end -----------")


class K1DayTest(unittest.TestCase):
    """测试1 day k 线图"""

    def setUp(self):
        config = get_config()
        self.email = "bottest@example.com"
        self.url = "https://" + config.get("host") + "/v1/market/bars/ETH_USDT/K_1_DAY"
        self.my_token = login(self.email)
        self.headers = get_headers(self.my_token)

    def test_get_k_1_day(self):
        """测试获取1 day k 线图成功"""
        response = requests.request("GET", self.url, headers=self.headers)
        print(response.text)
        self.assertEqual(200, response.status_code)
        self.assertEqual("success", response.json()['status'])
        self.assertIsNotNone(response.json()['data'])

    def tearDown(self):
        print("--------test k 1 day end -----------")


class K1WeekTest(unittest.TestCase):
    """测试1 week k 线图"""
    def setUp(self):
        config = get_config()
        self.email = "bottest@example.com"
        self.url = "https://" + config.get("host") + "/v1/market/bars/ETH_USDT/K_1_WEEK"
        self.my_token = login(self.email)
        self.headers = get_headers(self.my_token)

    def test_get_k_1_week(self):
        """测试获取1 week k 线图成功"""
        response = requests.request("GET", self.url, headers=self.headers)
        self.assertEqual(200, response.status_code)
        self.assertEqual("success", response.json()['status'])
        self.assertIsNotNone(response.json()['data'])

    def tearDown(self):
        print("--------test k 1 week end -----------")


if __name__ == "__main__":
    unittest.main(verbosity=2)