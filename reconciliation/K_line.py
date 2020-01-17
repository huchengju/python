
from decimal import *
import json
import  data_conn
import  get_database
import file_read_write


def get_trades_line():#获取交易数据
    config_ex=data_conn.config_init_("ex")
    conn = data_conn.pymysql.connect(**config_ex)
    #cur = conn.cursor()

    sql=get_database.get_orders_trades()
    trade_data=dict()
    try:
        frozenset=dict()
        cur = conn.cursor()
        cur.execute(sql)

        row = cur.fetchone()
        message=dict()
        while row is not None:
            a=[]
            mm=1
            if row['orderid'] is not None:
                message=json.loads(row['message'])

                #print(message.get('orderId'))
                #print(message.get('symbol'))
                #print(message.get('createdAt'))


                if message.get('matchedRecords') is not None:
                    #print(len( message.get('matchedRecords')))
                    trade=[]
                    trade= message.get('matchedRecords')
                    for mm in trade :
                    #while mm<= len( message.get('matchedRecords')):
                        #trade=message.get('matchedRecords')[mm-1:mm]
                        #print(mm.get('matchPrice'))
                        #print(mm.get('matchAmount'))
                        cur1 = conn.cursor()
                        str_sql=get_database.K_line(mm.get('matchAmount'),mm.get('matchPrice'),message.get('createdAt'),message.get('symbol'),message.get('orderId'))
                        cur1.execute(str_sql)
                        print(str_sql)


            row = cur.fetchone()
    except Exception as e:
		#cur.rollback()
		#cur.close()
	    print('Error')
	    raise e
    finally:
	    cur.close()
    conn.commit()
    conn.close()

get_trades_line()


