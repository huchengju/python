import requests
import json
import hmac
from interface.personal_account import ga_auth
from config.circumstance_config import get_config
from interface.common.get_sql_str import get_secret_key
from interface.common.get_data_from_db import get_user_id_by_email,get_conn_to_db,get_user_GA_secret
from interface.common import get_GA_code



# Filename: login.py
# author: yujie.li

def hmac_password(email, b_pass):
    h = hmac.new(email.encode('utf-8'), b_pass, "sha256")
    password = h.hexdigest()
    return password


def login(email):
    """根据email登录并拿到token"""
    config = get_config()
    base_url = "https://" + config.get("host") + "/v1/sign-in"
    headers = get_headers()

    # if email is None:
    #     email = "bottest@example.com"
    #     secretKey = "OFCSSHNSK47IL4TJJ4X4GYBUY3V7BMJS"
    #     ga = ga_auth.get_totp_token(secretKey)
    # else:
    #     email = email
    #     secretKey = check_bind_ga(email)
    #     if secretKey is None:
    #         ga = ""
    #     else:
    #         print(secretKey)
    #         # ga = ga_auth.get_totp_token(secretKey)
    #         userid = get_user_id_by_email(email)
    #         secretKey = get_user_GA_secret(userid).get("secretKey")
    #         ga = get_GA_code.get_google_code(secretKey)
    #     print(type(ga))
    email = email
    secretKey = check_bind_ga(email)
    if secretKey is None:
        ga = ""
    else:
        print(secretKey)
        # ga = ga_auth.get_totp_token(secretKey)
        userid = get_user_id_by_email(email)
        secretKey = get_user_GA_secret(userid).get("secretKey")
        ga = get_GA_code.get_google_code(secretKey)
        print(type(ga))
    password = hmac_password(email, b"Password01")
    payload = {"email": email, "password": password, "ga": ga}
    print("ga= " + str(ga))
    response = requests.request("POST", base_url, headers=headers, data=json.dumps(payload))
    status = response.json()['status']
    if status != "success":
        print("login fail！ response: " + response.text)
    else:
        print("login success, response: " + response.text)
        my_token = response.json()['data']['token']
        print("my_token=" + my_token)
        return my_token


def login_with_param(email):
    """根据email登录并拿到token"""
    config = get_config()
    # email = "bottest@example.com"
    password = hmac_password(email, b"Password01")
    headers = {
        'Accept': "application/json",
        'Content-Type': "application/json",
        'cache-control': "no-cache"
    }
    payload = {"email": email, "password": password, "ga": ""}
    base_url = "https://" + config.get("host") + "/v1/sign-in"
    response = requests.request("POST", base_url, headers=headers, data=json.dumps(payload))
    status = response.json()['status']
    if status != "success":
        print("login fail！ error_code:" + response.json()['code'])
    else:
        print("login success")
        my_token = response.json()['data']['token']
        print("my_token=" + my_token)
        return my_token


def get_headers(token=None):
    if token is None:
        headers = {
            'accept': "application/json",
            'content-type': "application/json",
        }
    else:
        headers = {
            'Accept': "application/json",
            'Content-Type': "application/json",
            'Authorization': token,
        }
    return headers


def check_bind_ga(email=None):
    userId = get_user_id_by_email(email)
    # print(userId)
    # print(type(userId))
    query_sql = get_secret_key(userId)
    row = get_conn_to_db("ui", query_sql)
    if row is not None:
        if row['userId'] is not None:
            global secretKey
            secretKey = row['secretKey']
            print(secretKey)
            return secretKey
    else:
        print("该用户没有绑定过GA")
        return None


if __name__ == "__main__":
    # login("bottest@example.com")

    # login("bot01@example.com")
    login("bot02@example.com")
    # is_bind_ga("bot02@example.com")
    # is_bind_ga("bot02@example.com")
    # check_bind_ga("bot02@example.com")
    # check_bind_ga()