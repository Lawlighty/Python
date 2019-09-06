import pymysql

localhot = 'localhost'
user = 'root'
psw = 'rootroot'
base = 'aaa'

class myDB():
    def __init__(self):
        self.localhot = 'localhost'
        self.user = 'root'
        self.psw = 'rootroot'
        self.base = 'aaa'
        self.table = 'md5_users'
        self.cursor = None
        self.db = None

    def connDB(self):
        self.db = pymysql.connect(self.localhot, self.user, self.psw, self.base)
        self.cursor = self.db.cursor()

    def closeDB(self):
        self.cursor.close()
        self.db.close()

    def insertDB(self, username, password):
        self.connDB()
        sql = 'insert ignore into {} values(%s,%s)'.format(self.table)
        try:
            self.cursor.execute(sql,(username,password))
            self.db.commit()
            print('插入成功')

        except Exception as e:
            self.db.rollback()
            print(e)
        finally:
            self.closeDB()

    def searchDB(self, username):
        self.connDB()
        res = None
        sql = 'select username,password from {} where username=%s;'.format(self.table)
        try:
            self.cursor.execute(sql, (username))
            result = self.cursor.fetchall()
            if result:
                res = result[0]
            return res

        except Exception as e:
            self.db.rollback()
            print(e)
        finally:
            self.closeDB()

if __name__ == '__main__':
    aa = myDB()
    # aa.insertDB('user12','123')
    res = aa.searchDB('law')
    print(res)
    print('用户名:',res[0])
    print('密码:', res[1])