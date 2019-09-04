import pymysql

def ConnDB():
    print('连接数据库')
    db = pymysql.connect('localhost','root','rootroot','pythonsql')
    cursor = db.cursor()
    return db,cursor


def CloseDB(db,cursor):
    cursor.close()
    db.close()
    print('数据库关闭')

def get_ip_list():
    ip_list = []
    sql = 'select * from ip_pool'
    db = None
    cursor = None
    try:
        db, cursor = ConnDB()
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            ip_list.append(row[0])
        return ip_list
    except Exception as e:
        print(e)
        db.rollback()
    finally:
        CloseDB(db,cursor)

if __name__ == '__main__':
    print(get_ip_list())