from config.db_config import config_init
import pymysql
from tools import data_sql_str
from tools import file_read_write


def check_useridavailable():#检查Match_Details中计算的费率及计价币种是否正确
    config_ex=config_init("ex")
    conn = pymysql.connect(**config_ex)
    cur = conn.cursor()
    sql=data_sql_str.get_accountspotavailable()
    try:
        frozenset=dict()
        cur = conn.cursor()
        cur.execute(sql)
        row = cur.fetchone()
        while row is not None:
            a=[]
            if row['userid'] is not None:
                userid=row['userid']
                currency=row['currency']
                id=repr(userid)+currency
                #print(id)
                a.append(row['userid'])
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
#print(check_useridavailable())


def check_available_compare():
    sql="select a.userId,a.balance,a.currency from spot_accounts a  where  a.type='SPOT_AVAILABLE'"
    config_ex=config_init("ex")
    conn = pymysql.connect(**config_ex)
    cur = conn.cursor()
    user_frozen=dict()
    user_frozen=check_useridavailable()
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
                    #print(str(row['userId'])+"TTTTTTTTT",userid,currency)
                    print("{} | {}".format(row, amount))
                    if float(row['balance'])==float(amount) :
                        print('SUCCESS：可用金额比对- - 用户'+str(row['userId'])+",币种"+row['currency']+'可用量比对一致！'+str(float(row['balance']))+","+str(float(amount)))
                        str1="SUCCESS：可用金额比对- - 用户"+str(row['userId'])+",币种"+row['currency']+'可用量比对一致！' +str(float(row['balance']))+","+str(float(amount))
                    else:
                        print('  ERROR：可用金额比对- - 用户'+str(row['userId'])+",币种"+row['currency']+'可用量比对不一致，请检查！'+str(float(row['balance']))+","+str(float(amount)))
                        str1='  ERROR：可用金额比对- - 用户'+str(row['userId'])+",币种"+row['currency']+'可用量比对不一致，请检查！'+str(float(row['balance']))+","+str(float(amount))
                    file_read_write.create_available_file(str1)
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


if __name__ == "__main__":
    check_available_compare()








