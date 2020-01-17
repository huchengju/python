import requests
import json
from config import global_variable,circumstance_config
from interface.common import login



def get_ieo_detail(ieoId,token=None):
    url = "http://"+circumstance_config.circumstance_config_init(global_variable.cir_var).get("host")+"/v1/ieo/queryIeoProjectDetailInfo?projectId="+repr(ieoId)
    print(url)
    if token == None:
        response = requests.request("GET", url)
    else:
        header = {"Content-Type": "application/json", "Authorization": token}
        response = requests.request("GET", url, headers=header)

    if response.json().get("status") != "success":
        print("get ieo detail fail! ,response: ", response.json())
    else:
        print("get ieo detail success!")
        return response.json()

def get_all_group_list(ieoId,pageSize="20",pageNumber="1",token=None):
    url = "http://" + circumstance_config.circumstance_config_init(global_variable.cir_var).get("host") + "/v1/ieo/getAllGroupList?projectId=" + repr(ieoId)+"&pageSize="+pageSize+"&pageNumber="+pageNumber
    print(url)
    if token == None:
        response = requests.request("GET", url)
    else:
        header = {"Content-Type": "application/json", "Authorization": token}
        response = requests.request("GET", url, headers=header)

    if response.json().get("status") != "success":
        print("get all group fail! ,response: ", response.json())
    else:
        print("get all group success!")
        return response.json()

def get_user_group(ieoId,token):
    url = "http://" + circumstance_config.circumstance_config_init(global_variable.cir_var).get(
        "host") + "/v1/ieo/getCurrentUserGroup?projectId=" + repr(ieoId)
    print(url)
    header = {"Content-Type": "application/json", "Authorization": token}
    response = requests.request("GET", url, headers=header)
    if response.json().get("status") != "success":
        print("get user group fail! ,response: ", response.json())
    else:
        print("get user group success!")
        return response.json()

def get_user_purchase_infos(ieoId,token):
    url = "http://" + circumstance_config.circumstance_config_init(global_variable.cir_var).get(
        "host") + "/v1/ieo/getCurrentUserGroup?projectId=" + repr(ieoId)
    print(url)
    header = {"Content-Type": "application/json", "Authorization": token}
    response = requests.request("GET", url, headers=header)
    if response.json().get("status") != "success":
        print("get user purchase fail! ,response: ", response.json())
    else:
        print("get user purchase success!")
        return response.json()


def user_ieo_purchase(token,ieoId,paymentCurrency,purchaseAmount,userType,num,groupNumber):
    url = "http://" + circumstance_config.circumstance_config_init(global_variable.cir_var).get(
        "host") + "/v1/ieo/userPurchase"
    print(url)
    header = {"Content-Type": "application/json", "Authorization": token}
    data = {"ieoCurrencyId":ieoId,"paymentCurrency":paymentCurrency,"purchaseAmount":purchaseAmount,"userType":userType,"num":num,"groupNumber":groupNumber}
    response = requests.request("POST", url, headers=header,data=json.dumps(data))
    print(data)
    if response.json().get("status") != "success":
        print("ieo purchase fail! ,response: ", response.json())
    else:
        print("ieo purchase success!")
        return response.json()
#
# def user_purchase_data():
#     data = {"ieoCurrencyId":100076,"paymentCurrency":"USDT","purchaseAmount":"1","userType":1,"num":None,"groupNumber":-1}
#     pass


if __name__ == "__main__":
    token = login.login("1001@1.com")
    # print(get_ieo_detail(100076))
    # print(get_ieo_detail(100076,token))
    # print(get_all_group_list(100076))
    # print("--------------------------------------")
    # print(get_all_group_list(100076,token=token))
    # print(get_user_group(100076,token))
    # print(get_user_purchase_infos(100076,token))
    print(user_ieo_purchase(token,100076,"USDT","2",1,None,-1))