import requests
import json
from config import circumstance_config,global_variable
from interface.ieo import ieo_info
from interface.common import manage_login


def create_ieo(token):
    url = "https://"+circumstance_config.manage_config_init(global_variable.cir_var).get("host")+"/v1/manage/ieo/createIeoCurrency"
    header = header = {"Content-Type":"application/json","Authorization":token}
    data = ieo_info.ieo_info
    response = requests.request("POST",url,headers = header,data = json.dumps(data))
    if response.json().get("status") != "success":
        print("create IEO fail! request data: ",json.dumps(data),"response: ",response.json())
    else:
        print("create IEO success!")
        return response.json()


if __name__ == "__main__":
    token = manage_login.manage_login_by_cir(global_variable.cir_var)
    # create_ieo(token)
