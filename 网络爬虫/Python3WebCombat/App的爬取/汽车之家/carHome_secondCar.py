# 爬取汽车之家二手车主页面 严选好车  ------本周上新
import requests
from lxml import etree


def getHtmlText(url):
    headers={
        'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Mobile/14D27 auto_iphone/9.12.5 nettype/wifi autohomeapp/1.0 (auto_iphone;9.12.5;tFE3RQtL8w7XbmvPFh6q4-EdvbEnm2lfY-NnSITwNPmuTVwrfYkRr30PG9XBR_pUzfMG_JX-DWfxF_iOZx-xpsJMf_O5y1HIPkBkkiA0JfORj6etqc4asg;10.2.1;iPhone;93D7B5D0A9D73338238053A32524F639)'

    }
    try:
        r = requests.get(url, headers=headers, verify=False)# verify=False因为请求的是https 协议，所以请求禁用证书验证!!
        r.raise_for_status()

        return r.text

    except Exception as e:
        print(e)

def getInfo(text):
    if text:
        doc = etree.HTML(str(text))
        titleList = [ '本周上新','家用轿车', '超值SUV', '准新车', '代步首选']
        for i in range(len(titleList)):
            series_lis = doc.xpath('//div[@id="series_{}"]/ul/li'.format(i+1))
            print(titleList[i])
            for li in series_lis:
                name = li.xpath('./a/div/h4/text()')[0]
                title = li.xpath('./a/p')[0]
                newtitle = str(title.xpath('string(.)')).replace(' ',"").replace('\n','')

                print(name)
                print(newtitle)
            print('*'*20)


if __name__ == '__main__':
    url = 'https://m.che168.com/youxuan/110000/110100/index.html?sourcename=mainapp&safe=1&isautoapp=1&pvareaid=107748'
    html = getHtmlText(url)
    getInfo(html)