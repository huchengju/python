import requests
from config.circumstance_config import get_config
from interface.common.login import login, get_headers



# Filename: change_pass_get_email.py
# author: yujie.li
def get_email(email):
    config = get_config()
    url = "https://" + config.get("host") + "/v1/json/user/email"
    # my_token = login("bot02@example.com")
    my_token = login(email)
    headers = get_headers(my_token)
    response = requests.request("GET", url, headers=headers)
    if "success" != response.json()['status']:
        print("change password get email error! error_code:" + response.json()['code'])
    else:
        print("change password get email ok !")


if __name__ == "__main__":
    get_email()