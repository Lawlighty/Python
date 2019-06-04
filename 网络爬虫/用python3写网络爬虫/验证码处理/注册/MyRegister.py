import requests
from lxml import etree
from PIL import Image
import pytesseract
import base64
from io import BytesIO

def parser_form(html):
    doc = etree.HTML(str(html))
    data = {}
    for i in doc.xpath('//form//input'):
        if i.get('name'):
            data[i.get('name')] = i.get('value')

    return data

def get_captcha_img(html):# 获得图片
    doc = etree.HTML(str(html))

    img_scr = doc.xpath('//*[@id="recaptcha"]/img/@src')[0].split(',')[-1]
    img_data = base64.b64decode(img_scr)
    img = Image.open(BytesIO(img_data))
    return img

def get_captcha(img): #解析获得验证码
    img = img.convert('L')
    # 图片黑白分离
    img = img.point(lambda x: 0 if x < 1 else 255, '1')

    captcha = pytesseract.image_to_string(img)
    return captcha

def myfun(url,first_name, last_name, e_mail,password):
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    session = requests.Session()
    html = session.get(url, headers=headers).text
    data = parser_form(html)
    data['first_name'] = first_name
    data['last_name'] = last_name
    data['email'] = e_mail
    data['password'] = password
    data['password_two'] = password

    img = get_captcha_img(html)
    captcha = get_captcha(img)
    data['recaptcha_response_field'] = captcha

    resp = session.post(url,data=data,headers=headers)

    succ =  'user/register'not in resp.url#网页进行了跳转----注册成功
    if not succ:

        errors = etree.HTML(str(resp.text)).xpath('//div[@class="error"]')
        print('Form Error:')
        print('\n'.join('{}:{}'.format(e.get('id'),e.text) for e in errors))
    else:
        print('注册成功 emial--{},password--{}'.format(e_mail,password))

if __name__ == '__main__':
    url = 'http://example.python-scraping.com/places/default/user/register'
    firstname = 'asdqq'
    lastname = '11123sa'
    e_mail = "121212qw@122.com"
    psw = '123456789'
    myfun(url,firstname,lastname,e_mail,psw)
