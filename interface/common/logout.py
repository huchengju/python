import requests
from interface.common.login import login,get_headers
from config.circumstance_config import get_config


# Filename: logout.py
# author: yujie.li
def logout(email):
    config = get_config()
    url = "https://" + config.get("host") + "/v1/sign-out"
    token = login(email)
    headers = get_headers(token)
    response = requests.request("POST", url, headers=headers)
    if "success" != response.json()["status"]:
        print("logout fail ,error info " + response.text)
    else:
        print("logout success " + response.text)
    return response


if __name__ == "__main__":
    logout("bottest@example.com")
