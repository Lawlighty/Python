#从代理网站获得ip
import requests
import lxml
import config
import threading
import time
from lxml.html import fromstring
import DataBase
import queue


def getHtmlText(url, timeout=config.timeout):
    try:
        r = requests.get(url, headers=config.base_headers, timeout=timeout).text
        # r.raise_for_status()
        # r.encoding = 'utf-8'
        # r = r.text
        # page_content = requests.get(url, headers = config.base_headers).text
    except Exception as e:
        print('error : ', e)
    return r

#获得ip
def getIp():
    ip_list = []
    #爬取网站
    for url_agent in config.url_agent_pool:
        #爬取页数
        for i in range(1, config.crawl_pagenum):
            page_content = getHtmlText(url_agent.format(pagenum=i) )
            page_tree = fromstring(page_content)

            trs = page_tree.xpath('//div[@id="list"]/table/tbody/tr')
            for tr in trs:
                ip = tr.xpath('.//td')[0].text
                port = tr.xpath('.//td')[1].text
                now_ip = '{ip}:{port}'.format(ip=ip, port=port)

                ip_list.append(now_ip)

    return ip_list


#验证获得的ip是否可用
def verifyIP(ip_list):

    verified_ip = []
    while len(ip_list)>0:
        ip_item = ip_list.pop()

        proxies = {
            'http':'http://'+ip_item,
        }

        # print('代理:',proxies)
        headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3650.400 QQBrowser/10.4.3341.400'
        }
        try:
            resp = requests.get(config.verifyip, headers=headers, proxies= proxies, timeout=config.timeout)
            if resp.status_code==200:
                verified_ip.append(ip_item)

        except Exception as e:
            print(e)
            continue


    return verified_ip

#多线程检验ip是否可用
def task(ip_queue,verified_queue):
    while not ip_queue.empty():
        ip_item = ip_queue.get()
        proxies = {
            "http": "http://{ip_item}".format(ip_item=ip_item),
            # "https": "https://{ip_item}".format(ip_item=ip_item)
        }
        try:
            response = requests.get(config.verifyip, headers=config.base_headers, proxies=proxies,
                                    timeout=config.timeout)
            if response.status_code == 200:
                verified_queue.put(ip_item)
        except Exception as e:
            print('error : ', e)


def verifyip_multithread(ip_list):
    #检验队列
    ip_queue = queue.Queue()
    #合格队列
    verified_queue = queue.Queue()
    thread_list = []

    for item in ip_list:
        ip_queue.put(item)
    for i in range(0, config.thread_num):
        t = threading.Thread(target=task, name='thread{}'.format(i), args=(ip_queue, verified_queue,))
        thread_list.append(t)
    for i in thread_list:
        i.start()
    for i in thread_list:
        i.join()
    verified_iplist = []
    while not verified_queue.empty():
        verified_iplist.append(verified_queue.get())
    return verified_iplist

#写入数据库
def data_persistence(verified_ip):
    DataBase.init()
    DataBase.insert_ip_list(verified_ip)

#更新数据
def refresh_db():
    DataBase.dropTable()
    ip_list =getIp()
    verified_list =verifyIP(ip_list)
    data_persistence(verified_list)
    print('更新完成')
    # data_persistence(new_list)

# if __name__ == '__main__':
#     ip_list = getIp()
#     verified_ip = verifyIP(ip_list)
#     data_persistence(verified_ip)


