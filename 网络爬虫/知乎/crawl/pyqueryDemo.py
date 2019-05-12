from pyquery import PyQuery as pq

html = '<div class="aa www"><div class="bb"><a href ="www.baidu.com"><span class="cc">WDNMD<em>aaaa</em></span></a></div></div>'
doc = pq(html)
url = doc('a').attr('href')
print(url)
str = doc('.aa.www .bb span').text()
print(str)
for i in range(5):
    if (doc('.ABC')):
        print('存在')
    else:
        print('没有')
        continue

