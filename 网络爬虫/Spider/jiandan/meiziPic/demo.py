from pyquery import PyQuery as pq
from lxml import etree
import re
html = """
    <div>
        <ul>
            <li class="cc">cc</li>
            <li>aa</li>
            <li>aa</li>
            <li>aa</li>
            <li class="dd">dd</li>
        </ul>
    </div>
"""

doc = pq(html)
doc = etree.HTML(str(doc))

lis = doc.xpath('//div/ul/li[not(@class)]/text()')
for li in lis:
    print(li)

src = 'https://manhua.qpic.cn/manhua_detail/0/19_23_58_fbaa1351fe05d84d4cfaa4ac844fc839_8693.jpg/0'
ss = src.split('/')[5].split('_')[-1]
print(ss)

sss = 'http://wx3.sinaimg.cn/large/0066r0bugy1g3a1nmqyc5j30u0143ac2.jpg'
name = sss.split('/')[4]
print(name)
mlist= {}
s ='www.baidu.com'
ylist = []
ylist.append(s)
print(ylist)
mlist['key'] =ylist
print(mlist)
for i in mlist['key']:
    print(i)

a = list(range(10))
a.reverse()
print(a)
print('aaa')

arr = [1,2,3]
print(arr)
arr.reverse()
print(arr)
aaa ='[30]'
aaa = re.sub('\D','',aaa)
print(aaa)