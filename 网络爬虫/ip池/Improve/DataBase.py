import config
import pymysql
#数据库操作

#初始化
def init():
    try:
        db = pymysql.connect(config.mysql_localhost, config.mysql_root, config.mysql_psw, config.mysql_dbname )
        cursor = db.cursor()
        sql = 'CREATE TABLE IF NOT EXISTS {}(ip_port varchar(30) primary key not null)'.format(config.mysql_tableName)

        cursor.execute(sql)

    except Exception as e:
        print(e)
        db.rollback()
    finally:
        db.close()

#插入ip数据
    #逐条插入
def insert_ip(ip_port):
    try:
        db = pymysql.connect(config.mysql_localhost, config.mysql_root, config.mysql_psw, config.mysql_dbname)
        cursor = db.cursor()
        #忽略数据插入
        sql = 'insert ignore into {} values("{}")'.format(config.mysql_tableName, ip_port)

        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
    finally:
        db.close()

    #列表插入
def insert_ip_list(ip_list):
    try:
        db = pymysql.connect(config.mysql_localhost, config.mysql_root, config.mysql_psw, config.mysql_dbname)
        cursor = db.cursor()
        for i in ip_list:
            sql = 'REPLACE into {} values("{}")'.format(config.mysql_tableName, i)

            cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
    finally:
        db.close()

def get_ip_list():
    ip_list = []
    try:
        db = pymysql.connect(config.mysql_localhost, config.mysql_root, config.mysql_psw, config.mysql_dbname)
        cursor = db.cursor()
        sql = 'select * from {}'.format(config.mysql_tableName)
        cursor.execute(sql)
        #收全部的返回结果行
        result = cursor.fetchall()
        for row in result:
            ip_list.append(row[0])

    except Exception as e:
        print(e)
        db.rollback()
    finally:
        db.close()
        return ip_list

def dropTable():
    try:
        db = pymysql.connect(config.mysql_localhost, config.mysql_root, config.mysql_psw, config.mysql_dbname)
        cursor = db.cursor()
        sql = 'drop table if exists {}'.format(config.mysql_tableName)
        cursor.execute(sql)
    except Exception as e:
        print(e)
        db.rollback()
    finally:
        db.close()


