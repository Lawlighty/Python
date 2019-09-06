from DB_op import myDB
from test_md5 import get_Enc

def resert():
    print('注册界面')
    username = str(input('>>输入用户名'))
    password = str(input('>>输入密码'))
    mm = myDB()
    res = mm.searchDB(username)
    if res:
        #已经注册
        print('已经注册用户名')
        resert()
    else:
        password = get_Enc(password)
        mm.insertDB(username, password)
    print(' login ok')

def login():
    mm = myDB()
    print('登录界面')
    username = str(input('>>输入用户名'))
    password = str(input('>>输入密码'))
    enc_password = get_Enc(password)
    res = mm.searchDB(username)
    if res:
        if enc_password == res[1]:
            print('ok 登录成功')
        else:
            print('密码错误')
            login()
    else:
        print('用户名错误')
        login()

if __name__ == '__main__':
    # resert()
    login()