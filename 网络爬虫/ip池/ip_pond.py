# url = 'https://www.xicidaili.com/nn/'         代理ip网站
import requests
from bs4 import BeautifulSoup
import random
import time

def getHtmlText(utl):
    proxies = {
         "http": "http://116.209.55.252:9999"
    }
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3650.400 QQBrowser/10.4.3341.400'}
    try:
        r = requests.get(url= url, headers= headers, proxies= proxies)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        print('get html error')


def getIpList(html,url):
    soup = BeautifulSoup(html, 'html.parser')
    ip_list = []
    table = soup.find('table', attrs={'id':'ip_list'})
    tr = table.find_all('tr')
    for i in range(1,len(tr)):
        td = tr[i].find_all('td')
        ip_addr = td[1].text+':'+td[2].text
        ip_ht = td[5].text
        ip_list.append(ip_addr)
        time.sleep(random.randint(0,3))

        for ip in ip_list:
            try:
                if ip_ht == 'HTTP':
                    proxy_host='http://'+ ip
                    proxies_list = {'http':proxy_host}
                elif ip_ht == 'HTTPS':
                    proxy_host = 'https://'+ ip
                    proxies_list = {'https':proxy_host}
                headers = {
                    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3650.400 QQBrowser/10.4.3341.400'}

                res = requests.get(url=url, proxies= proxies_list , headers=headers).raise_for_status()

            except Exception as e:
                print('ip{} 不可用'.format(ip))
                ip_list.remove(ip)

            else:
                ip = proxy_host
                with open('my_ip_pond.txt', 'a') as f:
                    f.write(ip+'\n')
                    print('写入ip:',ip)


if __name__ == '__main__':
    url = 'https://www.xicidaili.com/nn/'
    html = getHtmlText(url)
    getIpList(html, url)

