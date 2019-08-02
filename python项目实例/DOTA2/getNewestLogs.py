# 从官网获得最新的更新日志(最近八个)
import requests
from lxml import etree
import pdfkit
# import wkhtmltopdf
import os
import shutil
import sys
sys.path.append(r'C:\Users\Administrator\Desktop\python\Py_webSpider\github\IP_pond\Improve')
from getProxy import get_proxies
url= 'https://www.dota2.com.cn/news/gamepost/news_update/index.htm'

def getHtmlText(url):
    """
    获得网页源代码
    :param url: 网页链接
    :return: 网页内容
    """
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3719.400 QQBrowser/10.5.3715.400',
        'Referer': 'https://www.dota2.com.cn/news/index.htm',
    }
    proxies = get_proxies()
    try:
        r = requests.get(url, headers=headers, proxies=proxies, timeout=5)
        r.raise_for_status()
        # print('编码:',r.encoding)
        return r.text
    except Exception as e:
        print(e)


def getNewestLogsTxt( text):
    """
    获得网页中每项更新日志的内容
    :param text: 网页内容
    :return: 每项更新日志的内容保存为txt
    """
    print('qidong l ')
    doc = etree.HTML(str(text))
    alis = doc.xpath('//li[@class="pane active"]/a')
    for a in alis:
        title = a.xpath('.//*[@class="title"]/text()')[0]
        date = a.xpath('.//*[@class="date"]/text()')[0]
        log_url = a.xpath('./@href')[0]

        content = getDetailedInfo(log_url)
        content = title+'\t\t'+date+content
        yield {
            'title': title,
            'date': date,
            'content': content,
        }

def getNewestLogsPdf( text):
    """
    获得网页中每项更新日志的内容
    :param text: 网页内容
    :return: 每项更新日志的内容保存为pdf
    """
    doc = etree.HTML(str(text))
    alis = doc.xpath('//li[@class="pane active"]/a')
    for a in alis:
        title = a.xpath('.//*[@class="title"]/text()')[0]
        log_url = a.xpath('./@href')[0]
        intoPdf(log_url, title)


def getDetailedInfo(log_url):
    """
    获得日志详细信息
    :param log_url: 日志链接
    :return: 详细信息
    """
    text = getHtmlText(log_url)
    doc = etree.HTML(str(text))
    # content = doc.xpath('//div[@class="content"]//text()')
    content = "\n".join(doc.xpath('//div[@class="content"]//text()'))
    return content

def intoTxt(info):
    """
    写入txt文件
    :param info: 字典信息
    :return: 文件
    """
    file_name = r'F:/python项目实例/DOTA2/newestLogs/'+ info.get('title')+'.txt'
    with open(file_name, 'w',encoding='utf-8') as f:
        f.write(info['content'])
    print("{}文件创建成功".format(file_name))

def intoPdf(url,title):
    """
    把网页内容转换为pdf
    :param url: 网页url
    :param title: 标题
    :return: pdf文件
    """
    path_wk = r'D:\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wk)
    pdfkit.from_url(url, r'F:/python项目实例/DOTA2/newestLogs/' + title + '.pdf', configuration=config)
    print('{}图片保存成功'.format(title))

def cleanLogsDir():
    """
    清空日志文件夹中的内容
    :return: 空文件夹
    """
    rootdir = r'F:/python项目实例/DOTA2/newestLogs'
    filelist = os.listdir(rootdir)
    for i in filelist:
        # 将文件名映射成绝对路径
        filepath = os.path.join(rootdir, i)
        #判断是文件还是文件夹
        if os.path.isfile(filepath):#文件直接删除
            os.remove(filepath)
        else:
            # 若为文件夹，则删除该文件夹及文件夹内所有文件
            shutil.rmtree(filepath, True)
    print('日志文件夹清空成功')

def main():
    cleanLogsDir()
    text = getHtmlText(url)
    while True:
        choice = input('>>是否以pdf格式保存更新日志?(t/f)').lower()
        if choice == 't':
            getNewestLogsPdf(text)
            print('pdf格式保存更新日志完成')
            break

        elif choice == 'f':
            for dic in getNewestLogsTxt(text):
                intoTxt(dic)
            print('txt格式保存更新日志完成')
            break
        else:
            print('输入错误')
            continue

if __name__ == '__main__':
    main()