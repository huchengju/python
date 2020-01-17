import requests
import json
import time
from interface.common.login import login,get_headers,check_bind_ga
from config.circumstance_config import get_config
from interface.personal_account.ga_auth import get_totp_token
from interface.common.get_data_from_db import get_user_id_by_email,get_api_key_by_userid


# Filename: api_key_management.py
# author: yujie.li
"""本文件包含api_key功能涉及的API基础接口，添加testCase时调用相关接口即可"""


def get_api_keys(email):
    config = get_config()
    url = "https://" + config.get("host") + "/v1/user/api-keys"
    token = login(email)
    headers = get_headers(token)
    response = requests.request("GET", url, headers=headers)
    if "success" != response.json()["status"]:
        print("get api keys error, response= " + response.text)
    else:
        print("get api keys success, response= " + response.text)
    return response


def add_api_key(canTrade, canWithdraw, email):
    config = get_config()
    url = "https://" + config.get("host") + "/v1/user/api-keys"
    token = login(email)
    headers = get_headers(token)
    secretKey = check_bind_ga(email)
    if secretKey is None:
        ga = ""
        print("GA为空，请先绑定GA~~")
    else:
        print(secretKey)
        ga = get_totp_token(secretKey)
    description = "test_add_api_key_" + time.strftime("%Y-%m-%d_%H_%M_%S")
    payload = {"description":description,"ga": ga, "canRead":True,"canTrade":canTrade,"canWithdraw":canWithdraw,"ipRestriction":"*"}
    response = requests.request("POST", url, data=json.dumps(payload),headers=headers)
    if "success" != response.json()["status"]:
        print("add api key fail, response= " + response.text)
    else:
        print("add api key success, response= " + response.text)
    return response


def delete_api_key(email):
    config = get_config()
    url = "https://" + config.get("host") + "/v1/user/api-keys/delete"
    token = login(email)
    headers = get_headers(token)
    userid = get_user_id_by_email(email)
    apikey = get_api_key_by_userid(userid)
    print(apikey)
    payload = {"apiKey":apikey}
    response = requests.request("POST", url, data=json.dumps(payload),headers=headers)
    if "success" != response.json()["status"]:
        print("delete api key fail, response= " + response.text)
    else:
        print("delete api key success, response= " + response.text)
    return response


def edit_api_key(canTrade, canWithdraw,email):
    config = get_config()
    url = "https://" + config.get("host") + "/v1/user/api-keys/update"
    token = login(email)
    headers = get_headers(token)
    secretKey = check_bind_ga(email)
    if secretKey is None:
        ga = ""
        print("GA为空，请先绑定GA~~")
    else:
        print(secretKey)
        ga = get_totp_token(secretKey)
    userid = get_user_id_by_email(email)
    apikey = get_api_key_by_userid(userid)
    print(apikey)
    description = "test_add_api_key_edited_" + time.strftime("%Y-%m-%d_%H_%M_%S")
    payload = {"description":description,"ga":ga,"apiKey":apikey,"canRead":True,"canTrade":canTrade,"canWithdraw":canWithdraw,"ipRestriction":"*"}
    response = requests.request("POST", url, data=json.dumps(payload),headers=headers)
    if "success" != response.json()["status"]:
        print("edit api key fail, response= " + response.text)
    else:
        print("edit api key success, response= " + response.text)
    return response


if __name__ == "__main__":
    # add_api_key(True,True,"bot02@example.com")
    # get_api_keys("bot02@example.com")
    add_api_key(True, True,"bottest@example.com")
    # get_api_keys()
    # delete_api_key()
    # edit_api_key(True,True,"bot02@example.com")
