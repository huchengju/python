import redis
from config.global_variable import cir_var, DEV, redis_password_stage


# Filename: redis_config.py
# author: yujie.li


# redis_choice = "soda-regress"
redis_choice = cir_var

def redis_config_init():
    global redis_config
    if redis_choice == "soda-dev1":
        redis_config = redis.Redis(host='bitsoda-dev1{}.redis.rds.aliyuncs.com'.format("" if DEV else "-vpc"), password='YnxFxgPwieYo2GJyljIb', port=6389, decode_responses=True)
    if redis_choice == "soda-test":
        redis_config = redis.Redis(host='bitsoda-test{}.redis.rds.aliyuncs.com'.format("" if DEV else "-vpc"), password='YnxFxgPwieYo2GJyljIb', port=6379, decode_responses=True)
    if redis_choice == "soda-test":
        redis_config = redis.Redis(host='bitsoda-stage{}.redis.rds.aliyuncs.com'.format("" if DEV else "-vpc"), password=redis_password_stage, port=6379, decode_responses=True)
    if redis_choice == "soda-regress":
        redis_config = redis.Redis(host='bitsoda-regress{}.redis.rds.aliyuncs.com'.format("" if DEV else "-vpc"), password='9wH8&&EXuh1FFJdy', port=6379, decode_responses=True)
    return redis_config


def redis_config_pool_init():
    global redis_config
    if redis_choice == "soda-dev1":
        pool = redis.ConnectionPool(host='bitsoda-dev1{}.redis.rds.aliyuncs.com'.format("" if DEV else "-vpc"), password='YnxFxgPwieYo2GJyljIb', port=6379, decode_responses=True)
        redis_config = redis.Redis(connection_pool=pool)
    if redis_choice == "soda-test":
        pool = redis.ConnectionPool(host='bitsoda-test{}.redis.rds.aliyuncs.com'.format("" if DEV else "-vpc"), password='MO3WCcxBKaFSzcaHmBTG', port=6379, decode_responses=True)
        redis_config = redis.Redis(connection_pool=pool)
    if redis_choice == "soda-stage":
        pool = redis.ConnectionPool(host='bitsoda-stage{}.redis.rds.aliyuncs.com'.format("" if DEV else "-vpc"), password=redis_password_stage, port=6379, decode_responses=True)
        redis_config = redis.Redis(connection_pool=pool)
    if redis_choice == "soda-regress":
        pool = redis.ConnectionPool(host='bitsoda-regress{}.redis.rds.aliyuncs.com'.format("" if DEV else "-vpc"), password='9wH8&&EXuh1FFJdy', port=6379, decode_responses=True)
        redis_config = redis.Redis(connection_pool=pool)
    return redis_config
