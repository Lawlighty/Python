import pymysql

def connDB():
    db = pymysql.connect('localhost','root','rootroot','dazhongdianp')
    cursor = db.cursor()
    return db, cursor

def intoDB(db, cursor, table_name, k,v):
    sql = 'insert ignore into {}(uni_num,uni_name) values("{}","{}")'.format(table_name,k,v)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        print('error')

def sel_fromDb(db, cursor, table_name, k):
    sql = 'select uni_name from {} where uni_num="{}" '.format(table_name,k)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)
        return results[0][0]
    except Exception as e:
        db.rollback()
        print('search error')

def CloseDB(db):
    db.close()
