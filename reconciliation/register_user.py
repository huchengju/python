import json
from urllib import parse
import requests
import hashlib
import hmac
import base64
import circumstances_config
import data_conn
import get_database
import global_variable
def get_name(email):
    sql=get_database.get_usersigin(email)
    print(sql)
    config_ex=data_conn.config_init_("ui")
    conn = data_conn.pymysql.connect(**config_ex)
    try:
        cur = conn.cursor()
        cur.execute(sql)
        row = cur.fetchone()
        if row['email'] is not None:
            code=row['code']
    except Exception as e:
	    print('Error')
	    raise e
    finally:
	    cur.close()
    conn.close()
    return code

def registeruser_doactive(email):
    code=get_name(email)
    print(code)
    config=circumstances_config.config_init_(global_variable.cir_var)
    header={'Content-Type':'application/json'}

    url="http://"+config.get('host')+"/v1/register"
    #print(url)
    Data={'email':email,'code':get_name(email)}
    print(Data)
    #req=requests.post(url, headers=header,data =json.dumps(Data))
    req=requests.post(url, headers=header,data =json.dumps(Data))
    status=req.status_code
    #print(req.status_code)
    #print(req.json())
    if status==200:
        status_code="注册失败！错误代码："+repr(req.status_code);
    else:
        str=req.content.decode()
        #print(str)
        token_dict=json.loads(str)
        print(token_dict)
        if token_dict.get('status')=='success':
            print("注册成功！")


def registeruser():
    email="test01@dae.org"
    hc = hmac.new(email.encode('utf-8'),b"password","sha256")
    hash_bytes = hc.hexdigest()
    config=circumstances_config.config_init_("matrix")
    header={'Content-Type':'application/json','Accept-Language':'en'}
    print(header)
    url="http://"+config.get('host')+"/v1/vcode/register"
    print(url)
    Data={'email':email,'password':hash_bytes,'name':'test01'}
    print(Data)
    #req=requests.post(url, headers=header,data =json.dumps(Data))
    req=requests.post(url, headers=header,data =json.dumps(Data))
    status=req.status_code
    print(req.content)
    #print(req.json())
    #token_dict=dict()
    if status!=200:
        status_code="注册发送！错误代码"
        print(status_code)
    else:
        str=req.content.decode()
        #print(str)
        token_dict=json.loads(str)
        #print(token_dict)
        if token_dict.get('status')=='success':
            print("注册发送成功！")
            registeruser_doactive(email)

        else:
            print("注册发送失败！")

registeruser()



