import unittest
import requests
from config.circumstance_config import get_config
from interface.common.get_data_from_db import check_user_is_exited
from interface.common.login import login, get_headers
from interface.common.register import register_action


# Filename: operation_records_test.py
# author: yujie.li
class OperationRecordsTest(unittest.TestCase):
    """测试获取个人中心操作记录"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = "bot02@example.com"
        email = check_user_is_exited(self.email)
        if email is None:
            register_action(self.email)
        else:
            pass

    def setUp(self):
            config = get_config()
            self.url = "https://" + config.get("host") + "/v1/operation/records?pageNumber=1&pageSize=30"
            self.my_token = login(self.email)
            self.headers = get_headers(self.my_token)

    def test_get_operation_records_success(self):
        """登录成功，获取对应登录操作记录成功"""
        response = requests.request("GET", self.url, headers=self.headers)
        self.assertEqual(200, response.status_code)
        self.assertEqual("success", response.json()['status'])
        self.assertIsNotNone(response.json()['data'])
        self.assertEqual("USER_LOGIN", response.json()['data']['items'][0]['operation'])
        # self.assertEqual("CHANGE_PASSWORD", response.json()['data']['items'][0]['operation'])

    def tearDown(self):
        print("-------test  operation records end ------")


if __name__ == "__main__":
    unittest.main(verbosity=2)