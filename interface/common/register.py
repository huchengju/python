import requests
import json
import hmac
import pymysql.cursors
from config.circumstance_config import get_config
from config.db_config import config_init
from interface.common import get_sql_str, login


# Filename: register.py
# author: yujie.li
def get_vcode(email):
    sql=get_sql_str.get_register_code(email)
    config_ui = config_init("ui")
    conn = pymysql.connect(**config_ui)
    try:
        cur = conn.cursor()
        cur.execute(sql)
        row = cur.fetchone()
        print(row)
        if row['email'] is not None:
            code=row['code']
    except Exception as e:
        print('Error')
        raise e
    finally:
        cur.close()
    conn.close()
    return code


def hmac_password(email):
    h = hmac.new(email.encode('utf-8'), b"Password01", "sha256")
    password = h.hexdigest()
    return password


def register_vcode(email, refId=None):
    """获取注册时邮件vcode， 无邀请码时，可不填写refId"""
    config = get_config()
    password = hmac_password(email)  # 调用方法获取加密后的password
    headers = login.get_headers()
    if refId is None:
        payload ={
            "email": email,
            "password": password,
            "enhancedValidateRequest":{
                "challenge":"62234f6e396b3471802d33b7ef1a74f16f",
                "validate":"1e8986dd53879b284c4b16b53f8cd19f",
                "seccode":"1e8986dd53879b284c4b16b53f8cd19f|jordan",
                "id":"43de7e0f-f16f-4ddc-bc5a-7bbc770e52dc"
            }
        }
    else:
        payload = {
            "email": email,
            "password": password ,
            "enhancedValidateRequest":{
                "challenge":"62234f6e396b3471802d33b7ef1a74f16f",
                "validate":"1e8986dd53879b284c4b16b53f8cd19f",
                "seccode":"1e8986dd53879b284c4b16b53f8cd19f|jordan",
                "id": "43de7e0f-f16f-4ddc-bc5a-7bbc770e52dc"
            },
            "refId": refId
        }

    base_url = "https://" + config.get("host") + "/v1/vcode/register"
    response = requests.request("POST", base_url, headers=headers, data=json.dumps(payload))
    status = response.json()['status']
    if status != "success":
        print("get register code fail！ error_code:" + response.json()['code'])
    else:
        print("get register code success")
        reg_vcode = get_vcode(email)
        return reg_vcode


def register_action(email, refId=None):
    """注册时，有邀请码，可填写邀请码，无邀请码时，refId可不填"""
    config = get_config()
    vcode = register_vcode(email, refId)
    payload = {
        "email": str(email),
        "zone": "+08:00",
        "code": vcode
    }
    headers = {
        'Content-Type': "application/json",
    }
    url = "https://" + config.get("host") + "/v1/register"
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
    if "success" != response.json()["status"]:
        print("register error, response: " + response.text)
    else:
        print("register success, response: " + response.text)
        return response



def check_referrer(referrerCode):
    """check 邀请码在系统是否存在"""
    config = get_config()
    # referrerCode = "qK0TW62N"
    url = "https://" + config.get("host") + "/v1/check_referrer?referrerCode=" + referrerCode
    headers = login.get_headers()
    response = requests.request("GET", url, headers=headers)
    if "success" != response.json()["status"]:
        print("check referrer error, response: " + response.text)
    else:
        print("check referrer success, response: " + response.text)


if __name__ == "__main__":
    email = "09bot@example.com"
    # register_action(email,"YBw8YMMq")
    # get_vcode(email)
    # register_vcode(email,"YBw8YMMq")
    register_action(email)
