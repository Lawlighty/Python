# Python岗位分析报告
import requests
from openpyxl import Workbook
import time
import json

def get_json(url_start, url_parser, page_num, job_name):
    proxies = {
        "http": "117.172.147.171:38292"
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3650.400 QQBrowser/10.4.3341.400'
    }

    #表单提交数据
    #存放在 From Data中
    data = {'first':'false','pn':page_num, 'kd':job_name}
    s= requests.Session()
    s.get(url_start, headers= headers)
    myCookie = s.cookies
    response = s.post(url_parser, data, headers= headers, cookies= myCookie, timeout=3)
    text = json.loads(response.text)
    # json = requests.post(url, data, headers= headers).json()
    print(text)
    list_content= text['content']['positionResult']['result']
    info_list = []
    for i in list_content:
        #单个公司招聘信息
        info = []
        #选取特定信息, 若无则
        info.append(i.get('companyShortName', '无'))
        info.append(i.get('companyFullName', '无'))
        info.append(i.get('industryField', '无'))
        info.append(i.get('companySize', '无'))
        info.append(i.get('salary', '无'))
        info.append(i.get('city', '无'))
        info.append(i.get('education', '无'))

        info_list.append(info)

    return info_list

def main():
    job_name = 'python'
    wb = Workbook()

    for i in ['北京', '上海', '广州', '深圳', '杭州']:
        page_num = 1
        ws = wb.active
        ws.title = job_name

        #cookie 获取链接
        url_start ='https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
        # 从 General-->Request URl 中获得
        url_parser = 'https://www.lagou.com/jobs/positionAjax.json?city={}&needAddtionalResult=false'.format(i)



        while page_num < 2 :
            info = get_json(url_start, url_parser, page_num, job_name)
            page_num += 1
            time.sleep(3)
            print('休息一下')

            #写入数据
            for row in info:
                ws.append(row)

    wb.save('{}职位信息.xlsx'.format(job_name))
    print('OK')

if __name__ == '__main__':
    main()
