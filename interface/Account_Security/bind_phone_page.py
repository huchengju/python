import requests
from config import circumstance_config, global_variable
from interface.common import get_data_from_redis
import json


def bind_phone_send_message_api(country,phoneNumber,token):
    url = "https://" + circumstance_config.circumstance_config_init(global_variable.cir_var).get("host") + "/v1/user/phone/sendMessage"
    print(url)
    data = {"phoneNumber":phoneNumber,"country":country}
    header = {"Content-Type": "application/json","Authorization": token}
    print(header,data)
    response = requests.request("POST",url=url,headers = header,data = json.dumps(data))
    if response.json().get("status") != "success":
        print("bind_phone_send_message_api fail,response: ", response.json())
    else:
        print("bind_phone_send_message_api success!")
    return response.json()



def bind_phone_send_email_api(token):
    url = "https://" + circumstance_config.circumstance_config_init(global_variable.cir_var).get("host") + "/v1/vcode/bindPhone"
    print(url)
    # data = {}
    header = {"Content-Type": "application/json", "Authorization": token}
    response = requests.request("POST", url=url, headers=header)
    if response.json().get("status") != "success":
        print("bind_phone_send_email_api fail,response: ", response.json())
    else:
        print("bind_phone_send_email_api success!")
    return response.json()




def bind_phone_api(country,email_code,phone_message_code,phoneNumber,token):
    url = "https://" + circumstance_config.circumstance_config_init(global_variable.cir_var).get("host") + "/v1/user/phone/add"
    header = {"Content-Type":"application/json","Authorization":token}
    data = {"country":country,"phoneNumber":phoneNumber,"messageCode":phone_message_code,"emailCode":email_code}
    print(header,data)
    response = requests.request("POST",url,headers = header,data = json.dumps(data))
    if response.json().get("status") != "success":
        print("bind_phone_api fail,response: ", response.json())
    else:
        print("bind_phone_api success!")
    return response.json()



def bind_phone(userid,country,phoneNumber,token):
    bind_phone_send_email_api(token)
    email_code = get_data_from_redis.get_bind_phone_email_code_from_redis(userid)
    bind_phone_send_message_api(country,phoneNumber,token)
    phone_message_code = get_data_from_redis.get_bind_phone_message_code_from_redis(country,phoneNumber)
    response = bind_phone_api(country,email_code,phone_message_code,phoneNumber,token)
    if response.get("status") != "success":
        print("bind_phone fail,response: ", response)
    else:
        print("bind_phone success!")
    return response





