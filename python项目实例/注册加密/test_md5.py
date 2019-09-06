#MD5加密 解密 测试
import hashlib

my_salt = b'Law'
def get_Enc(psw):
    print('明文:',psw)
    enc = hashlib.md5(my_salt)
    enc.update(psw.encode('utf-8'))
    enc_password = enc.hexdigest()
    print('密文:',enc_password)
    return enc_password
if __name__ == '__main__':
    password = str(input('>>输入密码'))
    get_Enc(password)
