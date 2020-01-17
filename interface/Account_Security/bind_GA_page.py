from config import circumstance_config, global_variable
import requests
import json
from interface.common import get_data_from_db, get_GA_code, get_data_from_redis


def get_GA_secret_api(token):
    url = "https://" + circumstance_config.circumstance_config_init(global_variable.cir_var).get("host") + "/v1/google/user/security/getSecret"
    header = {"Content-Type":"application/json","Authorization":token}
    response = requests.request("GET",url,headers = header)
    print(response.json())
    if response.json().get("status") != "success":
        print("send GA secret fail,response: ",response.json())
    else:
        print("send GA secret success!")
    return response.json()



def bind_GA_send_email_api(token):
    url = "https://" + circumstance_config.circumstance_config_init(global_variable.cir_var).get("host") + "/v1/vcode/bind-ga"
    header = {"Content-Type":"application/json","Authorization":token}
    response = requests.request("POST",url,headers = header)
    if response.json().get("status") != "success":
        print("bind_GA_send_email_api fail,response: ",response.json())
    else:
        print("bind_GA_send_email_api success!")
    return response.json()


def bind_GA_api(email_code,GA_code,token):
    url = "https://" + circumstance_config.circumstance_config_init(global_variable.cir_var).get("host") + "/v1/google/user/security/bindGA"
    header = {"Content-Type":"application/json","Authorization":token}
    data = {"vcode":email_code,"code":GA_code}
    response = requests.request("POST",url,headers = header,data = json.dumps(data))
    if response.json().get("status") != "success":
        print("bind_GA_api fail,response: ",response.json())
    else:
        print("bind_GA_api success!")
    return response.json()


def bind_GA(email,token):
    get_GA_secret_api(token)
    userid = get_data_from_db.get_user_id_by_email(email)
    secret = get_data_from_db.get_bind_GA_secret_fromdb(userid)
    GA_code = get_GA_code.get_google_code(secret)
    bind_GA_send_email_api(token)
    email_code = get_data_from_redis.get_bind_GA_email_code_from_redis(userid)
    response = bind_GA_api(email_code, GA_code, token)
    if response.get("status") != "success":
        print("bind_GA fail,response: ", response)
    else:
        print("bind_GA success!")
    return response

