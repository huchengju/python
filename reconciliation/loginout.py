import json
from urllib import parse
import requests
import hashlib
import hmac
import base64
import circumstances_config
import global_variable
import login

def login_out(token):
    #token=login.get_Login('bot8@example.com');
    #print(token)
    header={'Content-Type':'application/x-www-form-urlencoded','Authorization':token}
    print(header)
    config=circumstances_config.config_init_(global_variable.cir_var)
    url="http://"+config.get('host')+"/v1/sign-out"
    print(url)
    #Data={}
    req=requests.post(url, headers=header)
    token_dict=dict()
    print(req.content.decode())
    if req.status_code!=200:
        print("登出失败！")
    else:
        str=req.content.decode()
        #print(str)
        token_dict=json.loads(str)
        if token_dict.get('status')=='success':
            print("登出成功!")
        else:
           print("登出失败!")
        #print("登出失败失败！"+req._content)
#token=login.get_Login('bot8@example.com');
#login_out(login.get_Login('bot8@example.com'))

