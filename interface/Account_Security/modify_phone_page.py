import json
import requests
from config import circumstance_config,global_variable
from interface.common import get_data_from_redis
from interface.Account_Security import bind_phone_page


def modify_phone_api(country,emailCode,messageCode,phoneNumber,token):
    url = "https://" + circumstance_config.circumstance_config_init(global_variable.cir_var).get("host") + "/v1/user/phone/modify"
    header = {"Content-Type":"application/json","Authorization":token}
    data = {"country":country,"phoneNumber":phoneNumber,"messageCode":messageCode,"emailCode":emailCode}
    print(header,data)
    response = requests.request("POST",url,headers = header,data = json.dumps(data))
    if response.json().get("status") != "success":
        print("modify_phone_api fail,response: ", response.json())
    else:
        print("modify_phone_api success!")
    return response.json()

def modify_phone(userid,country,phoneNumber,token):
    bind_phone_page.bind_phone_send_message_api(country,phoneNumber,token)
    messageCode = get_data_from_redis.get_bind_phone_message_code_from_redis(country,phoneNumber)
    bind_phone_page.bind_phone_send_email_api(token)
    emailCode = get_data_from_redis.get_bind_phone_email_code_from_redis(userid)
    response = modify_phone_api(country,emailCode,messageCode,phoneNumber,token)
    if response.get("status") != "success":
        print("modify_phone fail,response: ", response)
    else:
        print("modify_phone success!")
    return response
