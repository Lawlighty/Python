# 去掉urlhttps:中的s
import string
url = 'https://img.sgamer.com/dota2_sgamer_com/images/20140226/0ad345ef44a917ead6973664f2e55edc.jpg'
print(url)
#切片+拼接
new_url = url[:4]+url[5:]
print(new_url)

print('*'*20)
string = 'abc edf is good a '
tra = 'abd'
trb = '123'
#创建字符映射转换表
tran = str.maketrans(tra,trb)
aa = string.translate(tran)
print(aa)
print('*'*20)

