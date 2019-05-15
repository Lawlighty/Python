# 获得当前日期
import time
import datetime
import re

def getNowDate():
    nowdate = str(datetime.datetime.now()).split(' ')[0].split('-')
    year = int(nowdate[0])
    month = int(nowdate[1])
    date = int(nowdate[2])

    return year,month,date
y,m,d = getNowDate()

print('y:',y)
print('m:',m)
print('d:',d)