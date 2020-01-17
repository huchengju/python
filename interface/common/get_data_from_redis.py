import redis
from config import redis_config,global_variable
from interface.common import redis_key

def get_change_GA_emailcode_from_redis(userid):
    redis_config_data = redis_config.redis_config_init(global_variable.cir_var)
    conn = redis.Redis(**redis_config_data)
    key = redis_key.change_GA_email_code(userid)
    emailcode = conn.get(key).decode() if isinstance(conn.get(key), bytes) else conn.get(key)
    return emailcode


def get_bind_GA_email_code_from_redis(userid):
    redis_config_data = redis_config.redis_config_init(global_variable.cir_var)
    redis_conn = redis.Redis(**redis_config_data)
    key = redis_key.bind_GA_email_code_key(userid)
    email_code = redis_conn.get(key).decode()
    return email_code

def get_bind_phone_message_code_from_redis(country,phoneNumber):
    redis_config_data = redis_config.redis_config_init(global_variable.cir_var)
    redis_conn = redis.Redis(**redis_config_data)
    print("----------------------")
    key = redis_key.bind_phone_message_code_key(country, phoneNumber)
    print("bind_phone_message_code_key:",key)
    print(redis_conn.exists(key))
    message_code_value = redis_conn.get(key)
    print(message_code_value)
    message_code_value = message_code_value.decode() if isinstance(message_code_value, bytes) else message_code_value
    print(message_code_value)
    return message_code_value


def get_bind_phone_email_code_from_redis(userid):
    redis_config_data = redis_config.redis_config_init(global_variable.cir_var)
    redis_conn = redis.Redis(**redis_config_data)
    key = redis_key.bind_phone_email_code_key(userid)
    print(key)
    email_code = redis_conn.get(key).decode() if isinstance(redis_conn.get(key), bytes) else redis_conn.get(key)
    print(email_code)
    return email_code