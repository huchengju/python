
def bind_phone_message_code_key(country,phoneNumber):
    key = "PHONE::MESSAGE_CODE::"+repr(country)+repr(phoneNumber)
    return key

def bind_phone_email_code_key(userid):
    key = "VCODE:BIND_PHONE:"+repr(userid)
    return key

def bind_GA_email_code_key(userid):
    key = "VCODE:BIND_GA:"+repr(userid)
    return key

def bind_phone_message_key(country,phoneNumber):
    key = "PHONE::MESSAGE_CODE::"+repr(country)+repr(phoneNumber)
    return key

def change_GA_email_code(userid):
    key = "VCODE:CHANGE_GA:" + repr(userid)
    return key

def withdraw_phone_code_key(phone):
    # if phone is None:
    #     key = "withdraw_1357924680"
    # else:
    key = "withdraw_" + str(phone)
    print(key)
    return key


def withdraw_email_code_key(email):
    # if email is None:
    #     key = "withdraw_bottest@example.com"
    # else:
    key = "withdraw_" + email
    print("key="+key)
    return key


if __name__ == "__main__":
    withdraw_phone_code_key(1357924680)


