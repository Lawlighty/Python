import requests
from lxml import etree
import re

def getPos(x, html):
    pos = abs(int(re.search(r''+ x +' { background-position-x:(.*?)px }',html).group(1)))
    print('pppos:',pos)

doc = etree.HTML(html)
cmls = doc.xpath('//div[@class="row"]/div[@class="col-md-1"]')
for cml in cmls:
    lis = []
    NumClass = cml.xpath('./div/@class')
    for i in NumClass:
        code = str(i).split(' ')[0]
        getPos(code,html)
        # lis.append(code)
        # print(lis)
    print('---------')
# x = 'IB15OJR'
# patt = re.compile(r''+ x +' { background-position-x:-(.*?)px }')
# def getPos(x, html):
#     pos = int(re.search(r''+ x +' { background-position-x:-(.*?)px }',html).group(1))
#     print('pppos:',pos)
# pos = int(re.search(patt,html).group(1))
# num = None
# if pos<=15:
#     num = 0
# elif pos<=25:
#     num = 1
# elif pos<=35:
#     num = 2
# elif pos<=48:
#     num = 3
# elif pos<=60:
#     num = 4
# elif pos<=75:
#     num = 5
# elif pos<=87:
#     num = 6
# elif pos<=99:
#     num = 7
# elif pos<=113:
#     num = 8
# else:
#     num = 9
#
# print(pos)
# print(num)
