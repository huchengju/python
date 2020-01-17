import requests
import json
import hmac
from config import global_variable,circumstance_config,manage_account_config


def manage_login(email,password):
    url = "https://"+circumstance_config.manage_config_init(global_variable.cir_var).get("host")+"/v1/manage/sign-in"
    print(url)
    h = hmac.new(email.encode('utf-8'), password.encode('utf-8'), digestmod="sha256")
    password_AES = h.hexdigest()
    data = {"email":email,"password":password_AES}
    header = {"Content-Type":"application/json"}
    print(header,data)
    response = requests.request("POST",url,headers = header,data = json.dumps(data))
    if response.json().get("status") != "success":
        print("manage system login fail！")
    else:
        print("manage system login success！")
        return response.json().get("data").get("token")

def manage_login_by_cir(cir_var):
    account = manage_account_config.manage_init(global_variable.cir_var)
    email = account.get("manage_email")
    password = account.get("manage_password")
    return manage_login(email,password)


print(manage_login_by_cir(global_variable.cir_var))
