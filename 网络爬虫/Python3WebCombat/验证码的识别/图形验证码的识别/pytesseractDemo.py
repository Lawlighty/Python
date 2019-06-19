import requests
import pytesseract
from PIL import Image

def getCodePic(url):
    headers = {
        'user-agent': 'Mozilla/5.0'
    }
    try:
        r = requests.get(url,headers=headers)
        r.raise_for_status()
        with open('code.jpg', 'wb') as f:
            f.write(r.content)
        print('验证码保存完毕')
    except Exception as e:
        print(e)

def getCode():
    image = Image.open('code.jpg')
    #转化为灰度图像
    new_image = image.convert('L')
    #根据实际情况调整二值化阈值
    # 遍历图片像素点,如果点的值小于150,就设置为0,不然设置为255----黑(0)白(255)分离
    new_image = new_image.point(lambda x: 0 if x < 150 else 255, '1')
    new_image.save('newcode.jpg')

    captcha = pytesseract.image_to_string('newcode.jpg')
    print(captcha)

if __name__ == '__main__':
    url = 'http://my.cnki.net/elibregister/CheckCode.aspx'
    getCodePic(url)
    getCode()

