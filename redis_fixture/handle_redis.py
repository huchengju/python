from redis_fixture.redis_config import redis_config_pool_init


# Filename: handle_redis.py
# author: yujie.li

r = redis_config_pool_init()


def get_phone_message_code():
    phone_message_code = r.get('PHONE::MESSAGE_CODE::66676767')
    print(phone_message_code)
    return phone_message_code


def get_vcode_bind_phone():
    vcode_bind_phone = r.get("VCODE:BIND_PHONE:100008")
    # print(type(r.get("VCODE:BIND_PHONE:100023")))
    print(vcode_bind_phone)
    return vcode_bind_phone


def get_withdraw_code():
    withdraw_code = r.get("withdraw_bottest@example.com")
    print(withdraw_code)
    return withdraw_code


if __name__ == "__main__":
    # get_phone_message_code()
    # get_vcode_bind_phone()
    get_withdraw_code()



