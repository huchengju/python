import requests
import json
import hmac
import base64
from Crypto.Cipher import AES
from interface.common.login import login, get_headers, hmac_password
from config.circumstance_config import get_config


# Filename: findback_password.py
# author: yujie.li
def find_password_re_send(email):
    """重新发送验证码"""
    config = get_config()
    url = "https://" + config.get("host") + "/v1/json/finapassword_re_send"
    headers = get_headers()
    payload = {"email": email}
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
    if "success" != response.json()["status"]:
        print("findback password resend email error, response: " + response.text)
    else:
        print("findback password resend email success, response: " + response.text)


def findback_password(email):
    """找回密码发送验证码"""
    config = get_config()
    url = "https://" + config.get("host") + "/v1/json/findbackpassword"
    headers = get_headers()
    payload = {
        "email": email,
        "enhancedValidateRequest": {
            "challenge": "014c66cc91d20941d389e1969d31e5ea4q",
            "validate": "ccd019664487cb7c9078576e15fe7fed",
            "seccode": "ccd019664487cb7c9078576e15fe7fed|jordan",
            "id": "3d28c569-3904-4bb0-b4a2-20ccf1d53b96"
        }
    }
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
    if "success" != response.json()["status"]:
        print("findback password error, response: " + response.text)
    else:
        print("findback password success, response: " + response.text)


def findback_password_reset(email, vcode):
    """重置密码操作"""
    config = get_config()
    url = "https://" + config.get("host") + "/v1/json/findbackpassword/reset"
    headers = get_headers()
    # newPassword = "b5353dae1a439878a2d13bf54594465c23929d3c6238a39e7f0f59076deb9aff"
    newPassword = hmac_password(email, b"Password01")
    payload = {
        "email": email,
        "vcode": vcode,
        "newPassword": newPassword
    }
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
    if "success" != response.json()["status"]:
        print("reset password error , response: " + response.text)
    else:
        print("reset password success, response: " + response.text)


BS = 16
unpad = lambda s : s[0: - ord(s[-1])]


def decryptBase64(src):
    return base64.urlsafe_b64decode(src)


def decryptAES(src, key):
    src = decryptBase64(src)
    iv = b"01e481906ce0173202"
    cryptor = AES.new(key, AES.MODE_CBC, iv)
    text = cryptor.decrypt(src).decode()
    return unpad(text)


def aes_encryption(request):
    app_key = 'W7v4D60fds2Cmk2U'
    if request.method == 'POST':
        data = request.POST.get("data", "")
    else:
        return "error"
    decode = decryptAES(data, app_key)
    dict_data = json.loads(decode)
    return dict_data


if __name__ == "__main__":
    # find_password_re_send("bot04@example.com")
    # findback_password("bot04@example.com")

    # s =decryptAES("01e481906ce01732023de62408d4becad21c2dd3b7c9c63f4dc97a51c4833116f66e62329aae9dc0", "01e481906ce0173202")
    # print(s)
    findback_password("bot05@example.com")
    # findback_password("lantian70703843@qq.com")