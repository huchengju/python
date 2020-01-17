# Filename: db_config.py
# author: yujie.li

import pymysql
import pymysql.cursors
from config.global_variable import cir_var, DEV, mysql_password_stage



# cir_var = "soda-test"


def config_init(db_name):
    if cir_var == "soda-dev1" or cir_var == "manage-dev1":
        if db_name == "ex":
            db_config = {
                'host': 'bitsoda-dev1{}.mysql.rds.aliyuncs.com'.format("" if DEV else "-vpc"),
                'port': 3306,
                'user': 'bitsoda',
                'password': '1MvDH4RyKERTLscZ4qnV',
                'db': 'ex',
                'charset': 'utf8mb4',
                'cursorclass': pymysql.cursors.DictCursor,
            }
        if db_name == "hd":
            db_config = {
                # 'host': '161.117.112.108',
                'host': 'bitsoda-dev1{}.mysql.rds.aliyuncs.com'.format("" if DEV else "-vpc"),
                'port': 3306,
                'user': 'bitsoda',
                'password': '1MvDH4RyKERTLscZ4qnV',
                'db': 'hd',
                'charset': 'utf8mb4',
                'cursorclass': pymysql.cursors.DictCursor,
            }
        if db_name == "mg":
            db_config = {
                'host': 'bitsoda-dev1{}.mysql.rds.aliyuncs.com'.format("" if DEV else "-vpc"),
                'port': 3306,
                'user': 'bitsoda',
                'password': '1MvDH4RyKERTLscZ4qnV',
                'db': 'mg',
                'charset': 'utf8mb4',
                'cursorclass': pymysql.cursors.DictCursor,
            }
        if db_name == "ui":
            db_config = {
      'host': 'bitsoda-dev1{}.mysql.rds.aliyuncs.com'.format("" if DEV else "-vpc"),
                'port': 3306,
                'user': 'bitsoda',
                'password': '1MvDH4RyKERTLscZ4qnV',
                'db': 'ui',
                'charset': 'utf8mb4',
                'cursorclass': pymysql.cursors.DictCursor,
            }
        if db_name == "ieo":
            db_config = {
                'host': 'bitsoda-dev1{}.mysql.rds.aliyuncs.com'.format("" if DEV else "-vpc"),
                'port': 3306,
                'user': 'bitsoda',
                'password': '1MvDH4RyKERTLscZ4qnV',
                'db': 'ieo',
                'charset': 'utf8mb4',
                'cursorclass': pymysql.cursors.DictCursor,
            }
    if cir_var == "soda-test" or cir_var == "manage-test":
        if db_name == "ex":
            db_config = {
                'host': 'bitsoda-test{}.mysql.rds.aliyuncs.com'.format("" if DEV else "-vpc"),
                'port': 3306,
                'user': 'bitsoda',
                'password': 'YsFjxkgj5pZhPmFjEfdq',
                'db': 'ex',
                'charset': 'utf8mb4',
                'cursorclass': pymysql.cursors.DictCursor,
            }
        if db_name == "hd":
            db_config = {
                'host': 'bitsoda-test{}.mysql.rds.aliyuncs.com'.format("" if DEV else "-vpc"),
                'port': 3306,
                'user': 'bitsoda',
                'password': 'YsFjxkgj5pZhPmFjEfdq',
                'db': 'hd',
                'charset': 'utf8mb4',
                'cursorclass': pymysql.cursors.DictCursor,
            }
        if db_name == "mg":
            db_config = {
                'host': 'bitsoda-test{}.mysql.rds.aliyuncs.com'.format("" if DEV else "-vpc"),
                'port': 3306,
                'user': 'bitsoda',
                'password': 'YsFjxkgj5pZhPmFjEfdq',
                'db': 'mg',
                'charset': 'utf8mb4',
                'cursorclass': pymysql.cursors.DictCursor,
            }
        if db_name == "ui":
            db_config = {
                'host': 'bitsoda-test{}.mysql.rds.aliyuncs.com'.format("" if DEV else "-vpc"),
                'port': 3306,
                'user': 'bitsoda',
                'password': 'YsFjxkgj5pZhPmFjEfdq',
                'db': 'ui',
                'charset': 'utf8mb4',
                'cursorclass': pymysql.cursors.DictCursor,
            }
        if db_name == "ieo":
            db_config = {
                'host': 'bitsoda-test{}.mysql.rds.aliyuncs.com'.format("" if DEV else "-vpc"),
                'port': 3306,
                'user': 'bitsoda',
                'password': 'YsFjxkgj5pZhPmFjEfdq',
                'db': 'ieo',
                'charset': 'utf8mb4',
                'cursorclass': pymysql.cursors.DictCursor,
            }
    if cir_var == "soda-stage" or cir_var == "manage-stage":
        if db_name == "ex":
            db_config = {
                'host': 'bitsoda-stage{}.mysql.rds.aliyuncs.com'.format("" if DEV else "-vpc"),
                'port': 3306,
                'user': 'stage_user',
                'password': mysql_password_stage,
                'db': 'ex',
                'charset': 'utf8mb4',
                'cursorclass': pymysql.cursors.DictCursor,
            }
        if db_name == "hd":
            db_config = {
                'host': 'bitsoda-stage{}.mysql.rds.aliyuncs.com'.format("" if DEV else "-vpc"),
                'port': 3306,
                'user': 'stage_user',
                'password': mysql_password_stage,
                'db': 'hd',
                'charset': 'utf8mb4',
                'cursorclass': pymysql.cursors.DictCursor,
            }
        if db_name == "mg":
            db_config = {
                'host': 'bitsoda-stage{}.mysql.rds.aliyuncs.com'.format("" if DEV else "-vpc"),
                'port': 3306,
                'user': 'stage_user',
                'password': mysql_password_stage,
                'db': 'mg',
                'charset': 'utf8mb4',
                'cursorclass': pymysql.cursors.DictCursor,
            }
        if db_name == "ui":
            db_config = {
                'host': 'bitsoda-stage{}.mysql.rds.aliyuncs.com'.format("" if DEV else "-vpc"),
                'port': 3306,
                'user': 'stage_user',
                'password': mysql_password_stage,
                'db': 'ui',
                'charset': 'utf8mb4',
                'cursorclass': pymysql.cursors.DictCursor,
            }
        if db_name == "ieo":
            db_config = {
                'host': 'bitsoda-stage{}.mysql.rds.aliyuncs.com'.format("" if DEV else "-vpc"),
                'port': 3306,
                'user': 'stage_user',
                'password': mysql_password_stage,
                'db': 'ieo',
                'charset': 'utf8mb4',
                'cursorclass': pymysql.cursors.DictCursor,
            }
    if cir_var == "soda-regress" or cir_var == "manage-regress":
        if db_name == "ex":
            db_config = {
                'host': 'bitsoda-regress{}.mysql.rds.aliyuncs.com'.format("" if DEV else "-vpc"),
                'port': 3306,
                'user': 'bitsoda',
                'password': "4xm85pFlg2cQ0UajIFJD",
                'db': 'ex',
                'charset': 'utf8mb4',
                'cursorclass': pymysql.cursors.DictCursor,
            }
        if db_name == "hd":
            db_config = {
                'host': 'bitsoda-regress{}.mysql.rds.aliyuncs.com'.format("" if DEV else "-vpc"),
                'port': 3306,
                'user': 'bitsoda',
                'password': "4xm85pFlg2cQ0UajIFJD",
                'db': 'hd',
                'charset': 'utf8mb4',
                'cursorclass': pymysql.cursors.DictCursor,
            }
        if db_name == "mg":
            db_config = {
                'host': 'bitsoda-regress{}.mysql.rds.aliyuncs.com'.format("" if DEV else "-vpc"),
                'port': 3306,
                'user': 'bitsoda',
                'password': "4xm85pFlg2cQ0UajIFJD",
                'db': 'mg',
                'charset': 'utf8mb4',
                'cursorclass': pymysql.cursors.DictCursor,
            }
        if db_name == "ui":
            db_config = {
                'host': 'bitsoda-regress{}.mysql.rds.aliyuncs.com'.format("" if DEV else "-vpc"),
                'port': 3306,
                'user': 'bitsoda',
                'password': "4xm85pFlg2cQ0UajIFJD",
                'db': 'ui',
                'charset': 'utf8mb4',
                'cursorclass': pymysql.cursors.DictCursor,
            }
        if db_name == "ieo":
            db_config = {
                'host': 'bitsoda-regress{}.mysql.rds.aliyuncs.com'.format("" if DEV else "-vpc"),
                'port': 3306,
                'user': 'bitsoda',
                'password': "4xm85pFlg2cQ0UajIFJD",
                'db': 'ieo',
                'charset': 'utf8mb4',
                'cursorclass': pymysql.cursors.DictCursor,
            }
    return db_config

