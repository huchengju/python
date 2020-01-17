# Filename: get_sql_str.py
# author: yujie.li

def get_register_code(email):
    sql_str = "SELECT email, code FROM registration_requests WHERE email=" + repr(email)
    return sql_str


def get_user_email(userid):
    sql_str = "SELECT email, userid FROM user_profiles WHERE userid=" + repr(userid)
    return sql_str


def get_secret_key(userId):
    str = "select secretKey,userId from ga_auths where userId=" +repr(userId)
    return str


def get_userid(email):
    str = "select email, userId from user_profiles where email=" + repr(email)
    return str


def get_bind_GA_secretkey(userid):
    str = "SELECT * FROM `bind_requests` WHERE expiresAt > UNIX_TIMESTAMP(NOW())*1000 and userid = "+ repr(userid) +" ORDER BY createdAt DESC limit 1"
    return str

def get_userid_by_phoneNumber(phoneNumber):
    str = "SELECT * FROM `users` WHERE phone_number = "+repr(phoneNumber)
    return str

def get_address_id(user_id=None):
    if user_id is None:
        str = "SELECT * FROM withdraw_addresses WHERE userId=100118"
    else:
        str = "SELECT * FROM withdraw_addresses WHERE userId=" + repr(user_id)
    return str

def get_phoneNumber_by_userid(userid):
    str = "SELECT phone_number FROM `users` where id = " + repr(userid)
    return str

def check_email_isexist(email):
    str = "SELECT * FROM `user_profiles` WHERE email = " + repr(email)
    return str

def get_user_GA_secret(userid):
    str = "SELECT secretKey FROM `ga_auths` WHERE userId = " + repr(userid)
    return str


def get_api_key(userid=None):
    if userid is None:
        str = "SELECT * FROM api_key_auths  WHERE userId=100118 LIMIT 1"
    else:
        str = "SELECT * FROM api_key_auths WHERE userId=" + repr(userid) + " LIMIT 1"
    return str


def get_apcode_by_userid(userid):
    str = "SELECT ap_code FROM `users` where id = " + repr(userid)
    return str


def get_withdraw_record_by_userid(userid):
    str = "SELECT * FROM withdraw_requests WHERE userId=" + repr(userid) + " order by createdAt desc LIMIT 1"
    return str


def delete_user_profile_by_email(email):
    str = "DELETE from user_profiles WHERE email=" + repr(email)
    return str


def delete_registration_requests_by_email(email):
    str = "DELETE from registration_requests WHERE email=" + repr(email)
    return str

def delete_users_by_userid(userid):
    str = "DELETE from users WHERE id=" + repr(userid)
    return str

def delete_ga_auths_userid(userid):
    str = "DELETE from ga_auths WHERE userid=" + repr(userid)


def delete_bind_requests_by_userid(userid):
    str = "DELETE from bind_requests WHERE userid=" + repr(userid)
    return str


def get_ongoing_ieoId():
    str = "SELECT * FROM `currency_purchase_info` WHERE start_time < UNIX_TIMESTAMP(now())*1000 AND end_time > UNIX_TIMESTAMP(now())*1000 ORDER BY id DESC LIMIT 1"



