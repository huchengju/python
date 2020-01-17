import requests
from config import circumstance_config,global_variable


def get_banner_list(token=None):
    url = "https://"+circumstance_config.circumstance_config_init(global_variable.cir_var).get("host")+"/v1/ui/get_banner_list?type=BANNER&source=IEO"
    if token == None:
        response = requests.request("GET",url)
    else:
        header = {"Content-Type": "application/json", "Authorization": token}
        response = requests.request("GET", url,headers = header)

    if response.json().get("status") != "success":
        print("get banner list fail! ,response: ", response.json())
    else:
        print("get banner list success!")
        return response.json()

def get_ieo_list(token=None):
    url = "https://"+circumstance_config.circumstance_config_init(global_variable.cir_var).get("host")+"/v1/ieo/queryIeoProjectInfos"
    if token == None:
        response = requests.request("GET", url)
    else:
        header = {"Content-Type": "application/json", "Authorization": token}
        response = requests.request("GET", url, headers=header)

    if response.json().get("status") != "success":
        print("get ieo list fail! ,response: ", response.json())
    else:
        print("get ieo list success!")
        return response.json()



if __name__ == "__main__":
    print(get_banner_list())