import json
from urllib import parse
import requests
import hashlib
import hmac
import base64
import circumstances_config
import data_conn
import global_variable
import get_database
import google_ver
def get_email(userid):
    sql=get_database.get_username(userid)
    config_ex=data_conn.config_init_("ui")
    conn = data_conn.pymysql.connect(**config_ex)
    #cur = conn.cursor()
    email=""
    try:
        cur = conn.cursor()
        cur.execute(sql)
        row = cur.fetchone()
        if row['userId'] is not None:
           email=row['email']
    except Exception as e:
		#cur.rollback()
		#cur.close()
	    print('Error')
	    raise e
    finally:
	    cur.close()
    conn.close()

    return email

def get_Login(email):
    #email=get_email(userid)
    #print(email)
    status_code=0
    #matrix dev2
    config=dict()
    config=circumstances_config.config_init_(global_variable.cir_var)
    #print(config)
    hc = hmac.new(email.encode('utf-8'),b"password","sha256")
    hash_bytes = hc.hexdigest()
    header={'Content-Type':'application/json'}
    #Data={"email": email,"password":hash_bytes,"ga":"0000","next":""}
    Data={"email": email,"password":hash_bytes,"ga":google_ver.get_totp_token("FGJRYVYYPYHEBNTWDEMQRZKKOI2YIY6E")}
    print(Data)
    url="https://"+config.get('host')+"/v1/sign-in"
    #url="https://api-test.matrix.co/v1/sign-in"
    print(url)
    req=requests.post(url, headers=header,data =json.dumps(Data))
    status=req.status_code
    token_dict=dict()
    print(req.content)
    if status!=200:
        status_code="登录失败！错误代码："+repr(req.status_code);
        print(status_code)
    else:
        str=req.content.decode()
        #print(str)
        token_dict=json.loads(str)
        print(token_dict)
        print("登录成功！")
        return token_dict.get("data").get("token")
#print(get_Login('bot2@example.com'))

#print(get_email(99110))
#https://api-test.matrix.co/v1/sign-in