import requests
from lxml.html import fromstring
import lxml
import config
from getIpfromWeb import getHtmlText
from lxml import etree


url = 'https://www.kuaidaili.com/free/intr/2'
# url = 'https://www.xicidaili.com/nn/'
r = requests.get(url).text
# print(r)
ip_list = []
tree = fromstring(r)
trs = tree.xpath('//div[@id="list"]/table/tbody/tr')
for tr in trs:
    ip = tr.xpath('.//td')[0].text
    port = tr.xpath(".//td")[1].text
    my_ip = ip+':'+port
    ip_list.append(my_ip)
print(ip_list)

header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
    'Referer':'http://www.baidu.com'
}

dic ={
    'name':{
        'old':'mmm',
        'now':'ysq'

    },
    'add':{
        'old':'zho',
        'now':'shaxxx'
    }
}
# print(dic['name']['now'])

ip_list = []
# 爬取网站
