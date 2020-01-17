import pymysql
from config.db_config import config_init
# from config.get_sql_str import get_address_id


# query_sql = get_address_id(100118)


def get_conn_to_db(db_name, query_sql):
    """根据db_name，query_sql连接数据库并返回查询结果"""
    db_name_cofig = config_init(db_name)
    print(db_name_cofig)
    conn = pymysql.connect(**db_name_cofig)
    try:
        global cur
        cur = conn.cursor()
        cur.execute(query_sql)
        row = cur.fetchall()
    except Exception as e:
        print("error" + str(e))
        raise e
    finally:
        cur.close()
    conn.close()
    print("row = " + str(row))
    return row


# if __name__ == "__main__":
#     get_conn_to_db("ex",q uery_sql)