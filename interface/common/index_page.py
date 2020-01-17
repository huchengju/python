import requests
import json
from interface.common.login import get_config,get_headers,login


# Filename: index_page.py
# author: yujie.li
def get_symbol_data():
    """获取symbol data 数据"""
    config = get_config()
    url = "https://" + config.get("host") + "/v1/ui/symbol_data?baseSymbol=USDT"
    headers = get_headers()
    response = requests.request("GET", url, headers=headers)
    if "success" != response.json()["status"]:
        print("get symbol data error , response: " + response.text)
    else:
        print("get symbol data success, response: " + response.text)
        return response


def get_index_symbol():
    """获取index symbol数据"""
    config = get_config()
    url = "https://" + config.get("host") + "/v1/ui/index_symbol?limit=4"
    headers = get_headers()
    response = requests.request("GET", url, headers=headers)
    if "success" != response.json()["status"]:
        print("get index symbol error, response: " + response.text)
    else:
        print("get index symbol success, response: " + response.text)
        return response


def add_symobl_option(symbol, email):
    """添加favorite symbol option"""
    config = get_config()
    url = "https://" + config.get("host") + "/v1/ui/symbol/optional/add"
    token = login(email)
    headers = get_headers(token)
    # payload = {"symbols":["LTC_USDT"]}
    payload = {"symbols":[symbol]}
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
    if "success"!= response.json()["status"]:
        print("add favorite symbol option error , response: " + response.text)
    else:
        print("add favorite symbol option success, response: " + response.text)
        return response


def remove_symbol_option(symbol, email):
    """移除favorite symbol option"""
    config = get_config()
    url = "https://" + config.get("host") + "/v1/ui/symbol/optional/remove"
    token = login(email)
    headers = get_headers(token)
    payload = {"symbols": [symbol]}
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
    if "success"!= response.json()["status"]:
        print("remove favorite symbol option error , response: " + response.text)
    else:
        print("remove favorite symbol option success, response: " + response.text)
        return response


if __name__ == "__main__":
    # get_symbol_data()
    # get_index_symbol()
    # add_symobl_option("LTC_USDT")
    remove_symbol_option("LTC_USDT")
