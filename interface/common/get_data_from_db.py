import pymysql
from interface.common import get_sql_str
from config.db_config import config_init


# Filename: get_data_from_db.py
# author: yujie.li

# 通用连接数据库方法,传入db_name, query_sql, 返回row
def get_conn_to_db(db_name, query_sql):
    """根据db_name，query_sql连接数据库并返回查询结果"""
    db_name_config = config_init(db_name)
    conn = pymysql.connect(**db_name_config)
    try:
        global cur
        cur = conn.cursor()
        cur.execute(query_sql)
        row = cur.fetchone()
    except Exception as e:
        print("error" + str(e))
        raise e
    finally:
        cur.close()
    conn.close()
    print("row = " + str(row))
    return row


def update_table_data(db_name, execute_sql):
    """更新数据库表数据"""
    db_name_config = config_init(db_name)
    conn = pymysql.connect(**db_name_config)
    try:
        global cur
        cur = conn.cursor()
        cur.execute(execute_sql)
        conn.commit()
    except Exception as e:
        print("error" + str(e))
        raise e
    finally:
        cur.close()
    conn.close()


def get_address_id_by_user_id(user_id):
    """根据userId获取提现地址ID"""
    query_sql = get_sql_str.get_address_id(user_id)
    print(query_sql)
    row = get_conn_to_db("ex", query_sql)
    print(row)
    print(type(row))
    if row['userId'] is not None:
        global address_id
        address_id = row['id']
    return address_id


def get_user_id_by_email(email):
    """根据email获取userID"""
    query_sql = get_sql_str.get_userid(email)
    row = get_conn_to_db("ui", query_sql)
    if row is not None:
        if row['userId'] is not None:
            global user_id
            user_id = row['userId']
            return user_id
    else:
        print("该用户不存在，请确认是否存在该用户~~")


def get_bind_GA_secret_fromdb(userid):
    """获取绑定GA时的secretKey"""
    conn_data = config_init("ui")
    conn = pymysql.connect(**conn_data)
    cur = conn.cursor()
    cur.execute(get_sql_str.get_bind_GA_secretkey(userid))
    secret = cur.fetchone().get("bindData")
    cur.close()
    print("secret",secret)
    return secret


def get_userid_by_phoneNumber(phoneNumber):
    """根据手机号获取绑定的userid"""
    conn_data = config_init("ex")
    conn = pymysql.connect(**conn_data)
    cur = conn.cursor()
    # sql = "SELECT id FROM `users` WHERE phone_number = "+repr(phoneNumber)
    sql = get_sql_str.get_userid_by_phoneNumber(phoneNumber)
    cur.execute(sql)
    result = cur.fetchone()
    cur.close()
    print("result", result)
    return result


def get_phoneNumber_by_userid(userid):
    """根据userid获取绑定的手机号"""
    conn_data = config_init("ex")
    conn = pymysql.connect(**conn_data)
    cur = conn.cursor()
    sql = get_sql_str.get_phoneNumber_by_userid(userid)
    cur.execute(sql)
    result = cur.fetchone()
    cur.close()
    print("result", result)
    return result


def get_user_GA_secret(userid):
    """根据userid获取已绑定的secretKey"""
    conn_data = config_init("ui")
    conn = pymysql.connect(**conn_data)
    cur = conn.cursor()
    sql = get_sql_str.get_user_GA_secret(userid)
    cur.execute(sql)
    result = cur.fetchone()
    print("result", result)
    cur.close()
    return result


def get_apcode_by_userid(userid):
    """根据userid获取用户的防钓鱼码"""
    conn_data = config_init("ex")
    conn = pymysql.connect(**conn_data)
    cur = conn.cursor()
    sql = get_sql_str.get_apcode_by_userid(userid)
    cur.execute(sql)
    result = cur.fetchone()
    cur.close()
    print("result", result)
    return result


def get_api_key_by_userid(userid=None):
    """根据email获取userID"""
    query_sql = get_sql_str.get_api_key(userid)
    print(query_sql)
    row = get_conn_to_db("ex", query_sql)
    print(row)
    if row is not None:
        if row['userId'] is not None:
            global apiKey
            apiKey = row['apiKey']
            return apiKey
    else:
        print("该用户还没有创建过apikey，请确认~~")


def get_withdraw_amount_by_userid(userid):
    """根据userid获取提现记录中amount值"""
    query_sql = get_sql_str.get_withdraw_record_by_userid(userid)
    print(query_sql)
    row = get_conn_to_db("ex", query_sql)
    print(row)
    if row is not None:
        if row['userId'] is not None:
            global amount
            amount = row['amount']
            return amount
    else:
        print("该用户没有提现记录~~~")


def get_withdraw_id_by_userid(userid):
    """根据userid获取提现记录中id"""
    query_sql = get_sql_str.get_withdraw_record_by_userid(userid)
    print(query_sql)
    row = get_conn_to_db("ex", query_sql)
    print(row)
    if row is not None:
        if row['userId'] is not None:
            global withdrawId
            withdrawId = row['id']
            return withdrawId
    else:
        print("该用户没有提现记录~~~")


def get_withdraw_status_by_userid(userid):
    """根据userid获取提现记录中status值"""
    query_sql = get_sql_str.get_withdraw_record_by_userid(userid)
    print(query_sql)
    row = get_conn_to_db("ex", query_sql)
    print(row)
    if row is not None:
        if row['userId'] is not None:
            global status
            status = row['status']
            return status
    else:
        print("该用户没有提现记录~~~")

def get_ongoing_ieoid():
    """获取状态为进行中的ieoId"""
    conn_data = config_init("ieo")
    conn = pymysql.connect(**conn_data)
    cur = conn.cursor()
    sql = get_sql_str.get_ongoing_ieoId()
    cur.execute(sql)
    result = cur.fetchone()
    print("result:",result)
    return result







def check_user_is_exited(email):
    """根据email判断系统是否存在某个账户"""
    query_sql = get_sql_str.check_email_isexist(email)
    row = get_conn_to_db("ui", query_sql)
    if row is not None:
        if row['userId'] is not None:
            global user_email
            user_email = row['email']
            return user_email
    else:
        print("该用户不存在~~")


def delete_user(email):
    """根据email删除用户"""
    userid = get_user_id_by_email(email)
    # userId =
    # print(get_user_id_by_email(email))

    del_users_sql = get_sql_str.delete_users_by_userid(userid)
    del_ga_auths_sql = get_sql_str.delete_ga_auths_userid(userid)
    del_registration_requests_sql = get_sql_str.delete_registration_requests_by_email(email)
    del_bind_requests_sql = get_sql_str.delete_bind_requests_by_userid(userid)
    del_user_profile_sql = get_sql_str.delete_user_profile_by_email(email)


    update_table_data("ex", del_users_sql)
    print("delete users success")
    update_table_data("ui", del_ga_auths_sql)
    print("delete ga_auth success")
    update_table_data("ui", del_registration_requests_sql)
    print("delete registration_requests success")
    update_table_data("ui", del_bind_requests_sql)
    print("delete bind_requests success")
    update_table_data("ui", del_user_profile_sql)
    print("delete user_profile success")




if __name__ == "__main__":
    # get_user_id_by_email("lantian70703843@qq.com")
    # # get_user_id_by_email()
    # # sql = "select email, userId from user_profiles where email='bottest@example.com'"
    # # get_conn_to_db("ui",sql)
    # get_withdraw_amount_by_userid(100118)
    # get_withdraw_id_by_userid()
    # get_withdraw_status_by_userid()

    print(get_ongoing_ieoid().get("id"))
    delete_user("bottest@example.com")
    delete_user("bot02@example.com")




