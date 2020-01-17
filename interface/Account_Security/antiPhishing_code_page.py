import requests
import json
from config import circumstance_config,global_variable

def add_antiPhishing_code_api(apCode,GA_code,token):
    url = "https://"+circumstance_config.circumstance_config_init(global_variable.cir_var).get("host")+"/v1/user/antiPhishing/add"
    header = {"Content-Type":"application/json","Authorization":token}
    data = {"apCode":apCode,"gaCode":GA_code}
    response = requests.request("POST",url,headers = header,data = json.dumps(data))
    if response.json().get("status") != "success":
        print("add_antiPhishing_code_api fail,response: ",response.json())
    else:
        print("add_antiPhishing_code_api success!")
    return response.json()


def modify_antiPhishing_code_api(newApCode,oldApCode,GA_code,token):
    url = "https://"+circumstance_config.circumstance_config_init(global_variable.cir_var).get("host")+"/v1/user/antiPhishing/modify"
    header = {"Content-Type":"application/json","Authorization":token}
    data = {"newApCode":newApCode,"oldApCode":oldApCode,"gaCode":GA_code}
    response = requests.request("POST",url,headers = header,data = json.dumps(data))
    if response.json().get("status") != "success":
        print("modify_antiPhishing_code_api fail,response: ", response.json())
    else:
        print("modify_antiPhishing_code_api success!")
    return response.json()