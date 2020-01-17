import requests
import time
from interface.common.login import login, get_headers
from config.circumstance_config import get_config


# Filename: deposit.py
# author: yujie.li

"""本文件包含deposit页面涉及的API基础接口，添加testCase时调用相关接口即可"""


def get_deposit_address_and_record(currency, email):
    """获取用户单个币种的基本充值信息"""
    config = get_config()
    print(config)
    url = "https://" + config.get("host") + "/v1/user/deposit/address-and-record?currency=" + currency + "&limit=100"
    token = login(email)
    headers = get_headers(token)
    response = requests.request("GET", url, headers=headers)
    if "success" != response.json()['status']:
        print("get deposit info error, response:" + response.text)
    else:
        print("get deposit info success, response:" + response.text)
    return response


def get_deposit_record(currency, email):
    """获取充值记录"""
    config = get_config()
    url = "https://" + config.get("host") + "/v1/user/deposit/record?currency="+currency+"&pageSize=10&pageNumber=1&startTime=&endTime="
    token = login(email)
    headers = get_headers(token)
    response = requests.request("GET", url, headers=headers)
    if "success" != response.json()['status']:
        print("get deposit record error, response:" + response.text)
    else:
        print("get deposit record success, response:" + response.text)
    return response


if __name__ == "__main__":
    get_deposit_address_and_record("LTC", "bottest@example.com")
    # get_deposit_address_and_record("LTC")  # 默认是bottest@example.com

    # get_deposit_record("LTC")
    # get_deposit_record("BTC", "bot04@example.com")