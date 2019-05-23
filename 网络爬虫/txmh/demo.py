import re
import random
a =['https://manhua.qpic.cn/manhua_detail/0/19_23_56_9b0ac467ac503456f07a4eba990cbd00_8650.jpg/0']
b =[]
c =['https://manhua.qpic.cn/manhua_detail/0/19_23_56_30d52f8fd6d67de5d27494e91f86aa18_8651.jpg/0']
d =['https://manhua.qpic.cn/manhua_detail/0/19_23_56_5bef1ea29233803b57f6b1c70a3d6893_8652.jpg/0']

print(len(b))

href = 'https://manhua.qpic.cn/manhua_detail/0/19_23_56_9b0ac467ac503456f07a4eba990cbd00_8650.jpg/0'
href = href.split('_')[-1].split('/')[0]

print(href)

mlist = [ ['mztkn','diyizhang 1',['wwww.aaa.com','wwww.bbb.com']], ['mztkn','diyizhang 2',['wwww.ccc.com','wwww.ddd.com']]]
print('*'*20)
print(mlist)
for i in mlist:
    print(i)

