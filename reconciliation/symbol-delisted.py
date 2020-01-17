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
import login_manage



def delisted(symbol):
    tocken=login_manage.get_Login_manage()
    #print(tocken)
    #config=circumstances_config.config_init_(global_variable.cir_var)
    header={'Content-Type':'application/json','authorization':tocken }
    Data={}
    print(header)
    url="https://manage-new-test.matrix.co/v1/manage/symbol/stop"
    #url="https://api-test.matrix.co/v1/sign-in"
    print(url)
    req=requests.post(url, headers=header,data =Data)
    status=req.status_code
    token_dict=dict()
    print(req.content)
    if status!=200:
        status_code="退市错误！错误代码："+repr(req.status_code);
        print(status_code)
    else:
        str=req.content.decode()
        #print(str)
        token_dict=json.loads(str)
        print(token_dict)
        print("退市成功！")
        #return token_dict.get("data").get("token")



delisted("ETC_BTC")