import json
import random
import circumstances_config
import data_conn
import global_variable
import login
import get_database
import json
from urllib import parse
import requests
import login
import hashlib

def get_name(userid):
    sql=get_database.get_username(userid)
    config_ex=data_conn.config_init_("ui")
    conn = data_conn.pymysql.connect(**config_ex)
    try:
        cur = conn.cursor()
        cur.execute(sql)
        row = cur.fetchone()
        if row['userId'] is not None:
            email=row['email']
    except Exception as e:
	    print('Error')
	    raise e
    finally:
	    cur.close()
    conn.close()
    return email
def place_inorder():
    config=dict()
    config=circumstances_config.config_init_(global_variable.cir_var)
    print(config)
    for i in range(0,200000):
        #userid= random.randint(100080, 101049)
        userid= random.randint(102018, 102023)
        #userid=99010
        #userid=100065
        #print(userid)
        email=get_name(userid)
        token=login.get_Login(email)

        #print(token)
        amount= round(random.uniform(1, 2),8)
        #amount=0.23134
        symbol='BCH_BTC'
        #symbol=random.choice(['BCH_BTC','LTC_BTC','ZRX_BTC','ETH_BTC','ETC_BTC','BCH_ETH','ETC_ETH''LTC_ETH'])
        #symbol='ZRX_LTC'
        price= round(random.uniform(4,5),8)
        #price=5300.1714
        type=random.choice(['BUY_LIMIT','SELL_LIMIT','BUY_MARKET','SELL_MARKET'])
        #type=random.choice(['SELL_LIMIT'])
        #if type=='BUY_LIMIT':
            #price1=price+10
        #else:
            #price1=price-10
        header={'Content-Type':'application/json',"Authorization":token}
        #header={'Content-Type':'application/json',"Authorization":"AAAADGSL030000016bd6b6635bWEB6d63fcfc685ed74ad50dc938b3c18c075e3f58323d72c896ef1f5e2f5ed9422d"}
        #print(header)
        #Data={"amount": amount,"fillOrKill":False,"hidden":"False","immediateOrCancel":False,"mining":"","postOnly":False,"price":price,"source":"","symbol":symbol,"trailingStop":False,"triggerOn":0,"type":"BUY_LIMIT"}
        Data={"type":type,"symbol":symbol,"price":price,"amount":amount,"fillOrKill":False,"immediateOrCancel":False,"hidden":False,"postOnly":False}
        #Data={"price":price,"amount":amount,"total": "245","type":type,"symbol":symbol}

        #print(Data)
        url="https://"+config.get('host')+"/v1/trade/orders"
        #url="https://api-dev2.matrix.co/v1/trade/orders"
        print(url)
        #print(url1)
        req=requests.post(url, headers=header,data =json.dumps(Data))
        status=req.status_code
        #print(req.content)
        token_dict=dict()
        if status!=200:
            status_code="报单失败！错误代码："+repr(req.status_code);
        else:
            str=req.content.decode()
            #print(str)
            token_dict=json.loads(str)
            print("tttttttt",token_dict)
            print("报单成功！")
        #填写报单业务#

place_inorder()
