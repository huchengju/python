
import json
from urllib import parse
import requests
import hashlib
import hmac
import base64
#import circumstances_config
import data_conn
import global_variable
import get_database
import google_ver

def get_Login_manage():
    #email=get_email(userid)
    email="root@example.com"
    #print(email)
    status_code=0
    #matrix dev2
    config=dict()
    #config=circumstances_config.config_init_(global_variable.cir_var)
    #print(config)
    hc = hmac.new(email.encode('utf-8'),b"password","sha256")
    hash_bytes = hc.hexdigest()
    header={'Content-Type':'application/json'}
    #Data={"email": email,"password":hash_bytes,"ga":"0000","next":""}
    Data={"email": email,"password":hash_bytes}
    #print(Data)
    #url="https://"+config.get('host')+"/v1/sign-in"
    url="https://manage-new-test.matrix.co/v1/manage/sign-in"

    print(url)
    req=requests.post(url, headers=header,data =json.dumps(Data))
    status=req.status_code
    token_dict=dict()
    #print(req.content)
    if status!=200:
        status_code="登录失败！错误代码："+repr(req.status_code);
        print(status_code)
    else:
        str=req.content.decode()
        #print(str)
        token_dict=json.loads(str)
        #print(token_dict)
        print("登录成功！")
        return token_dict.get("data").get("token")
#print(get_Login('bot2@example.com'))

#print(get_email(99110))
#https://api-test.matrix.co/v1/sign-in


print(get_Login_manage())