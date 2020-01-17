import requests
import json
from config import circumstance_config,global_variable
from interface.common import get_data_from_redis,get_data_from_db,get_GA_code
from interface.Account_Security import bind_GA_page



def send_change_GA_email(token):
    url = "https://"+circumstance_config.circumstance_config_init(global_variable.cir_var).get("host")+"/v1/vcode/change-ga"
    header = {"Content-Type": "application/json", "Authorization": token}
    response = requests.request("POST", url, headers=header)
    if response.json().get("status") != "success":
        print("send_change_GA_email fail,response: ", response.json())
    else:
        print("send_change_GA_email success!")
    return response.json()




def change_GA_api(oldGACode,newGACode,vcode,token):
    url = "https://" + circumstance_config.circumstance_config_init(global_variable.cir_var).get("host") + "/v1/google/user/security/changeGA"
    header = {"Content-Type":"application/json","Authorization":token}
    data = {"oldGACode":oldGACode,"newGACode":newGACode,"vcode":vcode}
    print(header,data)
    response = requests.request("POST", url, headers=header, data=json.dumps(data))
    if response.json().get("status") != "success":
        print("change_GA_api fail,response: ", response.json())
    else:
        print("change_GA_api success!")
    return response.json()



def change_GA(userid,token):
    send_change_GA_email(token)
    vcode = get_data_from_redis.get_change_GA_emailcode_from_redis(userid)
    print("vcode",vcode)
    response = bind_GA_page.get_GA_secret_api(token)
    new_secret = get_data_from_db.get_bind_GA_secret_fromdb(userid)
    new_GA_code = get_GA_code.get_google_code(new_secret)
    # print("new_GA_code",new_GA_code)
    old_secret = get_data_from_db.get_user_GA_secret(userid).get("secretKey")
    old_GA_code = get_GA_code.get_google_code(old_secret)
    response = change_GA_api(old_GA_code,new_GA_code,vcode,token)
    if response.get("status") != "success":
        print("change_GA fail,response: ", response)
    else:
        print("change_GA success!")
    return response
