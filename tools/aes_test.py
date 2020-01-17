from Crypto.Hash import SHA256
from Crypto.Cipher import AES

# from Crypto.Cipher import AES
# import base64
#
#
# __encryptKey = "iEpSxImA0vpMUAabsjJWug=="
# __key = base64.b64decode(__encryptKey)
#     # AES加密
# def encrypt(data):
#     BS = 16
#     pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
#     cipher = AES.new(__key, AES.MODE_ECB)
#     encrData = cipher.encrypt(pad(data))
#     #encrData = base64.b64encode(encrData)
#     return encrData
#     # AES解密
# def decrypt(self,encrData):
#     #encrData = base64.b64decode(encrData)
#     #unpad = lambda s: s[0:-s[len(s)-1]]
#     unpad = lambda s: s[0:-s[-1]]
#     cipher = AES.new(self.__key, AES.MODE_ECB)
#     decrData = unpad(cipher.decrypt(encrData))
#     return decrData.decode('utf-8')


def encrypt():
    hash = SHA256.new()
    hash.update(b'message')
    h = hash.digest() #h = hash.hexdigest()
    print(h)

def encry_test():
    # 加密
    obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
    message = "The answer is no"
    ciphertext = obj.encrypt(message)
    print(ciphertext)



if __name__ == "__main__":
    # encrypt()
    encry_test()
