import random
import data_conn
import test
import get_database
import time
def place_inorder():
    config_ex=data_conn.config_init_("ex")
    #print(config_ex)
    conn = data_conn.pymysql.connect(**config_ex)
    #print(config_ex)
    cur = conn.cursor()
    #price=299.6000
    for i in range(0,20000):
        print(i)
        #cur = conn.cursor()
        #userid= random.randint(99000, 99999)
        userid=100023
        amount= round(random.uniform(0.01, 0.02),8)
        #amount=0.1
        #price=price-0.00001
        #amount=30
        #symbol=random.choice(['BTC_USDT','BCH_USDT','LTC_USDT','ETH_USDT','ETC_USDT','BCH_BTC','ETH_BTC','ETC_BTC','LTC_BTC','BTC_ETH','BCH_ETH','LTC_ETH','ETC_BCH'])
        #symbol=random.choice(['BCH_BTC','ETH_BTC','ETC_BTC','LTC_BTC','CTC_BTC'])
        symbol=random.choice(['BTC_USDT'])
        price=10564.54
        #price= round(random.uniform(1,2),8)
        #price=5300
        type=random.choice(['BUY_LIMIT','SELL_LIMIT','BUY_MARKET','SELL_MARKET'])
        #type=random.choice(['BUY_LIMIT'])
        #type=random.choice(['BUY_LIMIT'])
        #print(type)
        #if type=='BUY_LIMIT':
            #price1=price+10
            #type1='SELL_LIMIT'
        #else:
            #price1=price-10
            #type1='BUY_LIMIT'
        #print(price1)
        sql=get_database.get_userid_keySecret(userid)
        print(sql)
        try:
            #custom_sum = dict()g
            cur = conn.cursor()
            cur.execute(sql)
            row = cur.fetchone()
            while row is not None:
                if row['userId'] is not None:
                    #apikey=row['apiKey']
                    #apiSecret=row['apiSecret']
                    pram={"withdrawAddressId":24,"amount":0.1112,"currency":"ETC"}
                    data={}
                    #print(apikey,apiSecret,symbol)
                    DATA="withdrawAddressId=86&currency=ETC&amount=0.1"


                    apikey="AAAADBVXv0iwdBujTFS4XFFP"
                    apiSecret="lE0uLi4Yin1Qr3Ms"
                    client=test.ApiClient( apikey, apiSecret,"",True, 10,False);
                    print(client.post( "/v1/trade/orders",data,{"type":type,"symbol":symbol,"price":price,"amount":amount,"fillOrKill":False,"immediateOrCancel":False,"hidden":False,"postOnly":False})); #报单
                    #print(client.post("/v1/user/withdraw/submit",pram,{}));
                row = cur.fetchone()
        except Exception as e:
		    #cur.rollback()
		    #cur.close()
	        print('Error')
	        raise e
        finally:
	        #cur.close()
            print("这是一个测试")
    cur.close()
    conn.close()

place_inorder()



