import hmac
import base64
import struct
import hashlib
import time
import platform
import sys


def get_hotp_token(secret,intervals_no):
   key = base64.b32decode(secret, True)
   msg = struct.pack(">Q", intervals_no)
   h = hmac.new(key, msg, hashlib.sha1).digest()
   o = ord(chr(h[19])) & 15
   h = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % 1000000
   return h
def get_totp_token(secret):
   return get_hotp_token(secret, intervals_no=int(time.time())//30)

#print(get_totp_token("YTD3TLFIC3M4C7VFTCXI6G4QLXFV4ZYI"))

