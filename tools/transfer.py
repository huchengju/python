from config.circumstance_config import circumstance_config_init

from interface.common.login import get_headers,hmac_password
import requests
import json

# Filename: transfer.py
# author: yujie.li


global cir_var
cir_var = "manage-dev1"
global email
email = "root@example.com"

config = circumstance_config_init(cir_var)


def login_manage_system(email):
    """登录manage后台管理系统"""
    # config = circumstance_config_init(cir_var)
    password = hmac_password(email, b"password")
    print("password= "+ password)
    headers = get_headers()
    payload = {"email": email, "password": password}
    url = "https://" + config.get("host") + "/v1/manage/sign-in"
    print(url)
    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
    status = response.json()['status']
    if status != "success":
        print("manage system login fail！ response: " + response.text)
    else:
        print("manage system login success")
        my_token = response.json()['data']['token']
        print("my_token=" + my_token)
        return my_token


def get_account_id(userid, currency):
    # config = circumstance_config_init(cir_var)
    url = "http://" + config.get("host") + "/v1/account/batch/"+ str(userid) +"/"+ str(currency) +"/SPOT_AVAILABLE"
    global my_token
    my_token = login_manage_system(email)
    headers = get_headers(my_token)
    response = requests.request("GET", url, headers=headers)
    if "success" != response.json()['status']:
        print("get accountId error, response = " + response.text)
    else:
        if response.json()['data'] is not None:
            global accountId
            accountId = response.json()['data'][0]['id']
            print("get accountId success, accountId = " + str(accountId))
            return accountId


def do_transfer(toUserId, currency, amount):
    # config = circumstance_config_init(cir_var)
    url = "https://" + config.get("host") + "/v1/account/transfers"
    toAccountId = get_account_id(toUserId, currency)
    # 104 账户
    fromUserId = 104
    fromAccountId = get_account_id(fromUserId, currency)
    headers = get_headers(my_token)
    payload = {"transferType":"AVAILABLE_TO_AVAILABLE",
               "flowType":"ADJUST",
               "refType":"",
               "fromUserId":fromUserId,
               "fromAccountId":fromAccountId,
               "toUserIds":toUserId,
               "toAccountIds":toAccountId,
               "currency":currency,
               "amount":amount,
               "description":"test"
               }
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
    if "success" != response.json()['status']:
        print("transfer error , error_code = " + response.json()['code'])
    else:
        if response.json()['data'] is not None:
            print("transfer success!!")
            print(response.json()['data'])


def transfer_all(toUserId, amount):
    # amount = 5
    do_transfer(toUserId, "BTC", amount)
    do_transfer(toUserId, "LTC", amount)
    do_transfer(toUserId, "ETH", amount)
    do_transfer(toUserId, "BCH", amount)
    do_transfer(toUserId, "ETC", amount)
    do_transfer(toUserId, "CKB", amount)
    do_transfer(toUserId, "USDT",amount)


if __name__ == "__main__":
    # toUserId = 100122
    toUserId = 100013
    # currency = "BTC"
    # do_transfer(toUserId, "USDT", 3)

    transfer_all(100421, 100000)

    transfer_all(100013, 8)

    # login_manage_system("root@example.com")