
from decimal import *
import  data_conn
import  data_sql_str
import file_read_write


def check_useridfrozen():#检查Match_Details中计算的费率及计价币种是否正确
    config_ex=data_conn.config_init_("ex")
    conn = data_conn.pymysql.connect(**config_ex)
    cur = conn.cursor()
    sql=data_sql_str.sum_frozenamount_calculate()
    try:
        frozenset=dict()
        cur = conn.cursor()
        cur.execute(sql)
        row = cur.fetchone()
        while row is not None:
            a=[]
            if row['userId'] is not None:
                userid=row['userId']
                currency=row['currency']
                id=repr(userid)+currency
                #print(id)
                a.append(row['userId'])
                a.append(row['currency'])
                a.append(row['amount'])
                frozenset[id]=a
                #frozenset[id]=[row['userId'],row['currency'],row['amount']]

                #frozenset[id]=({"userid":row['userId'],"currency":row['currency'],"frozeen_amount":float(row['frozeen_amount'])})
                #feerate[orderid]=(str(row['makerFeeRate_calculate']),row['makerFeeRate'],float(row['takerFeeRate_calculate']),float(row['takerFeeRate']))
            row = cur.fetchone()
    except Exception as e:
		#cur.rollback()
		#cur.close()
	    print('Error')
	    raise e
    finally:
	    cur.close()
    conn.close()
    return frozenset
#check_useridfrozen()



def check_frozen_compare():
    sql="select a.userId,a.balance,a.currency from spot_accounts a  where  a.type='SPOT_FROZEN'"
    config_ex=data_conn.config_init_("ex")
    conn = data_conn.pymysql.connect(**config_ex)
    cur = conn.cursor()
    user_frozen=dict()
    user_frozen=check_useridfrozen()
    try:
        frozenset_sys=dict()
        cur = conn.cursor()
        cur.execute(sql)
        row = cur.fetchone()
        while row is not None:
            if row['userId'] is not None:
                userid=row['userId']
                currency=row['currency']
                id=repr(userid)+currency
                #print(id)
                #frozenset[id]=(row['userId'],row['currency'],row['balance'])
                #print (row['userId'],row['currency'],row['balance'])
                key=str(row['userId'])+row['currency']
                list_frozen=[]
                list_frozen=user_frozen.get(key)
                #print(list_frozen)
                if list_frozen!=None:
                    amount=repr(list_frozen[2:3])[10:len(repr(list_frozen[2:3]))-3]

                    #print(amount, row['balance'])
                    if float(row['balance'])==float(amount) :
                        print('SUCCESS用户'+str(row['userId'])+",币种"+row['currency']+'冻结金额比对一致！'+str(float(row['balance']))+","+str(float(amount)))
                        str1="SUCCESS：冻结金额比对- - 用户"+str(row['userId'])+",币种"+row['currency']+'冻结金额比对一致！'
                    else:
                        print('ERROR用户'+str(row['userId'])+",币种"+row['currency']+'冻结比对不一致，请检查！'+str(float(row['balance']))+","+str(float(amount)))
                        str1='  ERROR：冻结金额比对- - 用户'+str(row['userId'])+",币种"+row['currency']+'冻结金额比对不一致，请检查！'+str(float(row['balance']))+","+str(float(amount))

                    file_read_write.create_file(str1)
                #frozenset[id]=({"userid":row['userId'],"currency":row['currency'],"frozeen_amount":float(row['frozeen_amount'])})
                #feerate[orderid]=(str(row['makerFeeRate_calculate']),row['makerFeeRate'],float(row['takerFeeRate_calculate']),float(row['takerFeeRate']))
            row = cur.fetchone()
    except Exception as e:
		#cur.rollback()
		#cur.close()
	    print('Error')
	    raise e
    finally:
	    cur.close()
    conn.close()
    return frozenset

check_frozen_compare()








