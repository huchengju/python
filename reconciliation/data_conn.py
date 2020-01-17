import pymysql
import pymysql.cursors
import struct
import time
import global_variable
#####数据库连接字符串
def config_init_(dataname):
    #print(global_variable.cir_var)
    config_data=global_variable.cir_var
    #config_data="dev2"


    if  config_data=="dev1":
        #hose= 'api.highdax.com'
        #protocol="https"
        #origin="https://ui.highdax.com"
        #referer="https://ui.highdax.com/"
        if dataname=="ex":
            config= {
               'host':'bitsoda-dev1.mysql.rds.aliyuncs.com',
               'port':3306,
               'user':'bitsoda',
               'password':'1MvDH4RyKERTLscZ4qnV',
               'db':'ex',
               'charset':'utf8mb4',
               'cursorclass':pymysql.cursors.DictCursor,
               }
        if dataname=="hd":
            config= {
               'host':'bitsoda-dev1.mysql.rds.aliyuncs.com',
               'port':3306,
               'user':'bitsoda',
               'password':'1MvDH4RyKERTLscZ4qnV',
               'db':'hd',
               'charset':'utf8mb4',
               'cursorclass':pymysql.cursors.DictCursor,
               }
        if dataname=="mg":
            config= {
               'host':'bitsoda-dev1.mysql.rds.aliyuncs.com',
               'port':3306,
               'user':'bitsoda',
               'password':'1MvDH4RyKERTLscZ4qnV',
               'db':'mg',
               'charset':'utf8mb4',
               'cursorclass':pymysql.cursors.DictCursor,
               }
        if dataname=="ieo":
            config= {
               'host':'bitsoda-dev1.mysql.rds.aliyuncs.com',
               'port':3306,
               'user':'bitsoda',
               'password':'1MvDH4RyKERTLscZ4qnV',
               'db':'mg',
               'charset':'utf8mb4',
               'cursorclass':pymysql.cursors.DictCursor,
               }
        if dataname=="ui":
            config= {
               'host':'bitsoda-dev1.mysql.rds.aliyuncs.com',
               'port':3306,
               'user':'bitsoda',
               'password':'1MvDH4RyKERTLscZ4qnV',
               'db':'ui',
               'charset':'utf8mb4',
               'cursorclass':pymysql.cursors.DictCursor,
               }

    if  config_data=="test":

        if dataname=="ex":
            config= {
               'host':'bitsoda-test.mysql.rds.aliyuncs.com',
               'port':3306,
               'user':'bitsoda',
               'password':'YsFjxkgj5pZhPmFjEfdq',
               'db':'ex',
               'charset':'utf8mb4',
               'cursorclass':pymysql.cursors.DictCursor,
               }
        if dataname=="hd":
            config= {
               'host':'bitsoda-test.mysql.rds.aliyuncs.com',
               'port':3306,
               'user':'bitsoda',
               'password':'YsFjxkgj5pZhPmFjEfdq',
               'db':'hd',
               'charset':'utf8mb4',
               'cursorclass':pymysql.cursors.DictCursor,
               }
        if dataname=="mg":
            config= {
               'host':'bitsoda-test.mysql.rds.aliyuncs.com',
               'port':3306,
               'user':'bitsoda',
               'password':'YsFjxkgj5pZhPmFjEfdq',
               'db':'mg',
               'charset':'utf8mb4',
               'cursorclass':pymysql.cursors.DictCursor,
               }
        if dataname=="ieo":
            config= {
               'host':'bitsoda-test.mysql.rds.aliyuncs.com',
               'port':3306,
               'user':'bitsoda',
               'password':'YsFjxkgj5pZhPmFjEfdq',
               'db':'mg',
               'charset':'utf8mb4',
               'cursorclass':pymysql.cursors.DictCursor,
               }
        if dataname=="ui":
            config= {
               'host':'bitsoda-test.mysql.rds.aliyuncs.com',
               'port':3306,
               'user':'bitsoda',
               'password':'YsFjxkgj5pZhPmFjEfdq',
               'db':'ui',
               'charset':'utf8mb4',
               'cursorclass':pymysql.cursors.DictCursor,
               }

    if  config_data=="stage":

        if dataname=="ex":
            config= {
               'host':'bitsoda-stage.mysql.rds.aliyuncs.com',
               'port':3306,
               'user':'stage_user',
               'password':'PFB3eMiUbc2jia9JH4FNZPwU',
               'db':'ex',
               'charset':'utf8mb4',
               'cursorclass':pymysql.cursors.DictCursor,
               }
        if dataname=="hd":
            config= {
               'host':'bitsoda-stage.mysql.rds.aliyuncs.com',
               'port':3306,
               'user':'stage_user',
               'password':'PFB3eMiUbc2jia9JH4FNZPwU',
               'db':'hd',
               'charset':'utf8mb4',
               'cursorclass':pymysql.cursors.DictCursor,
               }
        if dataname=="mg":
            config= {
               'host':'bitsoda-stage.mysql.rds.aliyuncs.com',
               'port':3306,
               'user':'stage_user',
               'password':'PFB3eMiUbc2jia9JH4FNZPwU',
               'db':'mg',
               'charset':'utf8mb4',
               'cursorclass':pymysql.cursors.DictCursor,
               }
        if dataname=="ieo":
            config= {
               'host':'bitsoda-stage.mysql.rds.aliyuncs.com',
               'port':3306,
               'user':'stage_user',
               'password':'PFB3eMiUbc2jia9JH4FNZPwU',
               'db':'mg',
               'charset':'utf8mb4',
               'cursorclass':pymysql.cursors.DictCursor,
               }
        if dataname=="ui":
            config= {
               'host':'bitsoda-stage.mysql.rds.aliyuncs.com',
               'port':3306,
               'user':'stage_user',
               'password':'PFB3eMiUbc2jia9JH4FNZPwU',
               'db':'ui',
               'charset':'utf8mb4',
               'cursorclass':pymysql.cursors.DictCursor,
               }


    return config

#print(config_init_("ui"))