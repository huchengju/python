import requests
import time
from interface.personal_account import ga_auth
from interface.common.login import login, get_headers,check_bind_ga
from interface.common import get_data_from_db
from config.circumstance_config import get_config
from interface.common.redis_key import withdraw_email_code_key,withdraw_phone_code_key
from redis_fixture.redis_config import redis_config_pool_init



# Filename: withdraw.py
# author: yujie.li

"""本文件包含withdraw功能涉及的API基础接口，添加testCase时调用相关接口即可"""

r = redis_config_pool_init()



def withdraw_get_email_code(email):
    """获取withdraw email code，入参：email， 默认入参email=bottest@example.com"""
    config = get_config()
    url = "https://" + config.get("host") + "/v1/user/withdraw/send-email-code?type=withdraw"
    token = login(email)
    headers = get_headers(token)
    time.sleep(1)
    response = requests.request("GET", url, headers=headers)
    global withdraw_email_code
    if "success" != response.json()['status']:
        print("withdraw get email code error, response:" + response.text)
    else:

        withdraw_email_code = r.get(withdraw_email_code_key(email))
        print("withdraw get email code success, withdraw_email_code = " + str(withdraw_email_code))
    return withdraw_email_code


def withdraw_get_phone_code(phone, email):
    """获取withdraw时 phone code，入参：phone， email， 默认入参email=bottest@example.com,phone=1357924680"""
    config = get_config()
    url = "https://" + config.get("host") + "/v1/user/withdraw/send-phone-code?type=withdraw"
    token = login(email)
    headers = get_headers(token)
    time.sleep(1)
    response = requests.request("GET", url, headers=headers)
    global withdraw_phone_code
    if "success" != response.json()['status']:
        print("withdraw get phone code error, response:" + response.text)
    else:

        withdraw_phone_code = r.get(withdraw_phone_code_key(phone))
        print("withdraw get phone code success, withdraw_phone_code = " + str(withdraw_phone_code))
    return withdraw_phone_code


def withdraw_add_address(currency, address, email):
    """添加提现地址,入参：currency，address，email，默认email=bottest@example.com"""
    config = get_config()
    # currency = "BTC"
    # address = "mgsDuwXenPVsJfHFdRqsMkRFtTcjjEQiVJ"
    url = "https://" + config.get("host") + "/v1/user/withdraw/add-withdraw-address?currency=" + currency + "&description=" + currency + "&address=" + address
    token = login(email)
    headers = get_headers(token)
    time.sleep(1)
    response = requests.request("POST", url, headers=headers)
    if "success" != response.json()['status']:
        print("withdraw add address error, response:" + response.text)
    else:
        print("withdraw add address success, response:" + response.text)
    return response


def withdraw_delete_address(currency, email):
    """删除提现地址,入参：currency，email ，默认email=bottest@example.com"""
    config = get_config()
    token = login(email)
    time.sleep(1)
    user_id = get_data_from_db.get_user_id_by_email(email)
    address_id = get_data_from_db.get_address_id_by_user_id(user_id) # 获取address_id
    print("address_id" + str(address_id))
    url = "https://" + config.get("host") +"/v1/user/withdraw/delete-withdraw-address?currency=" + currency +"&addressId=" + str(address_id)
    headers = get_headers(token)
    time.sleep(1)
    response = requests.request("POST", url, headers=headers)
    if "success" != response.json()['status']:
        print("withdraw delete address error, response:" + response.text)
    else:
        print("withdraw delete address success, response:" + response.text)
    return response


def get_withdraw_records(currency, email):
    """获取withdraw页面info, 入参：currency， email; 默认email=bottest@example.com"""
    config = get_config()
    url = "https://" + config.get("host") + "/v1/user/withdraw/records?currency="+currency
    token = login(email)
    headers = get_headers(token)
    response = requests.request("GET", url, headers=headers)
    if "success" != response.json()["status"]:
        print("get withdraw records fail, response: " + response.text)
    else:
        print("get withdraw records success , response: " + response.text)
    return response


def get_day_amount(email):
    config = get_config()
    url = "https://" + config.get("host") + "/v1/user/withdraw/get-day-amount"
    token = login(email)
    headers = get_headers(token)
    response = requests.request("GET", url, headers=headers)
    if "success" != response.json()["status"]:
        print("get day amount fail ,response: " + response.text)
    else:
        print("get day amount success, response: " + response.text)
    return response


def get_fex(fromBase, toBase):
    config = get_config()
    url = "https://" + config.get("host") + "/v1/fee?fromBase=" + fromBase +"&toBase=" + toBase
    headers = get_headers()
    response = requests.request("GET",url, headers=headers)
    if "success" != response.json()["status"]:
        print("get fex error,response: " + response.text)
    else:
        print("get fex success, response: " + response.text)
        print("fromBase=" + fromBase)
        print("toBase=" + toBase)
    return response



def withdraw_action(amount, currency, address, phone, email):
    config = get_config()
    token = login(email)
    headers = get_headers(token)
    emailCode = withdraw_get_email_code(email)
    mobileCode = withdraw_get_phone_code(phone, email)
    secretKey = check_bind_ga(email)
    if secretKey is None:
        print("该用户未绑过GA,无法提现")
    else:
        ga_code = ga_auth.get_totp_token(secretKey)
        url = "https://" + config.get("host") + "/v1/user/withdraw/submit?amount=" + str(amount) + "&currency=" + currency + "&withdrawAddressId=&withdrawAddressStr=" + address + "&emailCode="+emailCode+"&gaCode="+ga_code+"&mobileCode=" + mobileCode
        print("***********")
        print(url)
        print("**************")
        response = requests.request("POST", url, headers=headers)
        if "success" != response.json()["status"]:
            print("withdraw error,response: " + response.text)
        else:
            print("withdraw success, response: " + response.text)
        return response


def cancel_withdraw(email):
    config = get_config()
    token = login(email)
    userid = get_data_from_db.get_user_id_by_email(email)
    withdrawId = get_data_from_db.get_withdraw_id_by_userid(userid)
    url = "https://" + config.get("host") + "/v1/user/withdraw/cancel?withdrawId=" + str(withdrawId)
    headers = get_headers(token)
    if withdrawId is None:
        print("该用户没有提现记录，无法做取消提现记录操作")
    else:
        response = requests.request("POST", url, headers=headers)
        if "success" != response.json()["status"]:
            print("cancel withdraw error,response: " + response.text)
        else:
            print("cancel withdraw success, response: " + response.text)
        return response


if __name__ == "__main__":
    # currency = "BTC"
    # address = "mgsDuwXenPVsJfHFdRqsMkRFtTcjjEQiVJ"
    # withdraw_add_address(currency, address, "bot04@example.com")
    # withdraw_add_address(currency, address)   #添加地址

    # withdraw_delete_address(currency, "bot04@example.com")
    # withdraw_delete_address(currency)  # 默认bottest@example.com  ，删除地址


    # withdraw_get_email_code("bot04@example.com")
    # withdraw_get_phone_code(1357924680)
    # withdraw_get_phone_code("bottest@example.com")
    # get_day_amount()
    # get_fex("BTC", "USDT")

    # withdraw_add_address("LTC","mwewY6WqmYuuQ9xvm9wr5ZP6PsrUPvFdPV", "bottest@example.com")
    # withdraw_action(1,"LTC","mwewY6WqmYuuQ9xvm9wr5ZP6PsrUPvFdPV",1357924680,"bottest@example.com")
    #
    # cancel_withdraw()
    withdraw_get_phone_code("1357924680", "bottest@example.com")




