from config.global_variable import cir_var, DEV, redis_password_stage

def redis_config_init(redis_name):
    if redis_name == "soda-dev1":
        redis_config = {
            "host" : "bitsoda-dev1{}.redis.rds.aliyuncs.com".format("" if DEV else "-vpc"),
            "port": 6379,
            "password":"YnxFxgPwieYo2GJyljIb"
        }
    if redis_name == "soda-stage":
        redis_config = {
            "host" : "bitsoda-stage{}.redis.rds.aliyuncs.com".format("" if DEV else "-vpc"),
            "port": 6379,
            "password":redis_password_stage
        }
    if redis_name == "soda-regress":
        redis_config = {
            "host" : "bitsoda-regress{}.redis.rds.aliyuncs.com".format("" if DEV else "-vpc"),
            "port": 6379,
            "password":"9wH8&&EXuh1FFJdy"
        }
    return redis_config


