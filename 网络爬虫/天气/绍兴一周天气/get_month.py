# 获得月份
import re
# date = str(input('date>'))
date = '201905'
month = re.findall('\d{4}(.)(.)', date)[0]
m1 = month[0]
m2 = month[1]
print(m1)
print(m2)