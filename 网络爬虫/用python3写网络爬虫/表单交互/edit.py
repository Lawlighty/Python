#登录表单之后     提交表单数据 更新表单数据
import requests
from lxml import etree

# 目标 url = 'http://example.python-scraping.com/places/default/edit/Afghanistan-1'
def login(login_url, url):
    session = requests.Session()
    data = {}
    html = session.get(login_url)
    cookie = html.cookies
    doc = etree.HTML(str(html.content))
    for i in doc.xpath('//form//input'):
        if i.get('name'):
            data[i.get('name')] = i.get('value')

    data['email'] = '123456@163.com'
    data['password'] = '123456abc'
    #登录
    session.post(login_url, data=data, cookies=cookie)
    #编辑页面
    resp = session.get(url)
    data = {

    }
    doc = etree.HTML(str(resp.content))
    for i in doc.xpath('//form//input'):
        if i.get('name'):
            data[i.get('name')] = i.get('value')
    # print(resp.text)
    print(data)

def myLogin(login_url, session=None):
    if session is None:
        resp = requests.get(login_url)
    else:
        resp = session.get(login_url)

    data = parser_form(resp.text)
    data['email'] = '123456@163.com'
    data['password'] = '123456abc'
    if session is None:
        cookie = resp.cookies
        resp = requests.post(login_url,data=data,cookies=cookie)
    else:
        resp = session.post(login_url, data)

    return resp, session
#解析表单
def parser_form(html):
    data = {}
    doc = etree.HTML(str(html))
    for i in doc.xpath('//form//input'):
        if i.get('name'):
            data[i.get('name')] = i.get('value')
    return data

def mydeit(resp):
    data = parser_form(resp.text)
    # print(data)
    data['population'] = 29121888

    return data

if __name__ == '__main__':
    login_url = 'http://example.python-scraping.com/user/login'
    edit_url = 'http://example.python-scraping.com/places/default/edit/Afghanistan-1'
    # login(login_url, url)
    # fun(url)
    session = requests.Session()
    resp, session = myLogin(login_url,session)
    resp = session.get(edit_url)

    data = parser_form(resp.text)
    print('当前表单:',data)

    data = mydeit(resp) #修改表单
    resp = session.post(edit_url, data)

    doc = etree.HTML(str(resp.text))

    area = doc.xpath('//*[@id="places_population__row"]/td[2]/text()')[0]
    print('修改后:')
    print('Population: ',area)

    session.close()

