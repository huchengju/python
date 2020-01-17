import requests
import unittest


# Filename: get_deposit_record_test.py
# author: yujie.li
class GetDepositRecordTest(unittest.TestCase):
    """测试获取充值进度情况"""
    def setUp(self):
        config = get_config()
        url = "https://" + config.get("host") + "/v1/user/deposit/address-and-record?currency=LTC&limit=100"
        token = login()
        headers= get_headers(token)
