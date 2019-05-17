import requests
from lxml import etree
from pyquery import PyQuery as pq

import sys
sys.path.append(r'C:\Users\Administrator\Desktop\python\Py_webSpider\github\IP_pond\Improve')
from getProxy import get_proxies

url = 'https://home.cnblogs.com/u/Yang-Sen'


def getHtmlText(url):
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3676.400 QQBrowser/10.4.3505.400',
    }
    cookies={
        'cookie':'_ga=GA1.2.1409714415.1554703585; __gads=ID=a5304af261dcd4c2:T=1554703585:S=ALNI_MbEsW4VT55Z3ElVFspuBPVYP8Thwg; UM_distinctid=16a1ec92e0bca-04c3b65518f387-4d764416-100200-16a1ec92e0c138; __utma=226521935.1409714415.1554703585.1556871669.1556871669.1; __utmz=226521935.1556871669.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _gid=GA1.2.839933537.1557463307; .Cnblogs.AspNetCore.Cookies=CfDJ8JcopKY7yQlPr3eegllP76ONU4DW7YjCWy40gI6hf9myPV5ajk7NVExemnfstB1tbKJF2OyOqLT2GisTVjvl4bcF-mn-4aXJ52G2n2gLQBobFwxenWoyAOvcGa13hlH32dXrq_PuOyuhgHXcH2nby0WfC7cPTAQTYOdCy7YW805ZP5e3ZT3ALtIt_0_2Vft90hmllh3jNhNPMlCJPejJlz2EXsNhEyWS1KjFXxJ84fNM_zoF6xhU7Kj4sCn9vHhfg3B7SznY0qaTT5f0uCEeIhrD1gZn4YPIP-QBLG2JVoA6O1gkhLwcl-Vw-WweKjuAS0VbMVgo4J_bF9qAVqWuphAWls-CdFR-dqwcIHA-Sj3PFpiKh1givGqsthFY4Pf6lZyRhCNU_Aopac48afzKxU9Oi6S-zeVx0iy07UmG7CF5vXFH4DT_Dtkmsam_Yd4nkQ; .CNBlogsCookie=70A254D254EC0CB9FD627D2B7FE7A278AF297DD82AD19D643B5D263438C4195FAF708B086BE305CC124EDD70B8A126ABF076B337AE4F8CCEB35326582BAE6F7A0565B1554A33A5982F7E83150ED7CB57F9173534; _gat=1'
    }
    proxies= get_proxies()
    try:
        r = requests.get(url, headers=headers, proxies=proxies, cookies=cookies)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text

    except Exception as e:
        print(e)


def getInfo(html):
    doc = pq(html)
    doc = etree.HTML(str(doc))

    feed_items =doc.xpath('//*[@id="feed_list"]/ul/li')
    for item in feed_items:
        feed_title = item.xpath('div[2]/div[1]/a[2]/text()')[0]
        feed_url = item.xpath('div[2]/div[1]/a[2]/@href')[0]
        feed_desc = item.xpath('div[2]/div[2]/text()')[0]

        # print('title:'+feed_title)
        # print('url:' + feed_url)
        # print('desc:'+feed_desc)

        with open('Blogs.txt','a+', encoding='utf-8') as f:
            f.write('Sean_Yang 发表博客:'+feed_title+'\t'+'url:'+feed_url+'\n')
            f.write('描述:'+'\n'+'\t'+feed_desc+'\n\n\n')



if __name__ == '__main__':
    text = getHtmlText(url)
    getInfo(text)