import hmac
import base64
import struct
import hashlib
import time
# from random import choice
# import string
import pyotp
import random
from qrcode import QRCode


# Filename: ga_auth.py
# author: yujie.li
def get_hotp_token(secret, intervals_no):
    key = base64.b32decode(secret, True)
    msg = struct.pack(">Q", intervals_no)
    h = hmac.new(key, msg, hashlib.sha1).digest()
    o = ord(chr(h[19]))& 15
    h = (struct.unpack(">I", h[o:o+ 4])[0]& 0x7fffffff)% 1000000
    return h


def get_totp_token(secret):
    googlecode = get_hotp_token(secret, intervals_no=int(time.time())// 30)
    return '%06d' % googlecode


# 生成二维码的函数
def get_qrcode(data, *args, **kwargs):
    qr = QRCode(*args,**kwargs)
    qr.add_data(data)
    im = qr.make_image()
    im.show()


def main():
    gtoken = pyotp.random_base32() # google token value
    print(gtoken)

    t = pyotp.TOTP(gtoken)
    print(t.now())
    print(get_totp_token(gtoken))

    email = "xyz@xyz.com"
    get_qrcode(email)