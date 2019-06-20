from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from io import BytesIO
from PIL import Image
from selenium.webdriver import ActionChains
import sys
sys.path.append(r'C:\Users\Administrator\Desktop\python\Py_webSpider\Python3WebCombat\验证码的识别\点触验证码的识别\Chaojiying_Python\chaojiying_Python')
from chaojiying import Chaojiying_Client


USERNAME = ''
PASSWORD = ''
CHAOJIYING_USER = '1'
CHAOJIYING_PSW = 'l'
CHAOJIYING_SOFT_ID = 900078
CHAOJIYING_KIND = 9102

class Crack12306():

    def __init__(self):
        self.url = 'https://kyfw.12306.cn/otn/resources/login.html'
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 20)
        self.email = USERNAME
        self.password = PASSWORD
        self.chaojiying = Chaojiying_Client(CHAOJIYING_USER,CHAOJIYING_PSW,CHAOJIYING_SOFT_ID)
        self.pic_id = None

    def openWeb(self):
        """
        打开网页输入用户名密码
        :return:
        """
        self.browser.get(self.url)
        self.browser.maximize_window()
        #选择账号密码登录
        bb = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.login-hd-account > a')))
        bb.click()
        time.sleep(1)
        username = self.browser.find_element_by_id('J-userName')
        username.send_keys(self.email)
        password = self.browser.find_element_by_id('J-password')
        password.send_keys(self.password)

    def get_12306_element(self):
        """
        获取验证码图片对象
        :return:图片对象
        """
        element = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'imgCode')))
        return element

    def get_position(self):
        """
        获取验证码位置
        :return:位置元祖
        """
        element = self.get_12306_element()
        time.sleep(2)
        location = element.location
        size = element.size
        top,buttom,left,right = location['y'], location['y']+size['height'], location['x'],location['x']+size['width']
        return top, buttom, left, right

    def get_web_shot(self):
        """
        获得整个网页截图
        :return: 图片对象
        """
        web_shot = self.browser.get_screenshot_as_png()
        web_shot = Image.open(BytesIO(web_shot))
        return web_shot

    def get_captach_img(self):
        """
        根据验证码坐标位置从网页截图中截取验证码图片
        :return:验证码图片
        """
        top, buttom, left, right = self.get_position()
        print('验证码位置', top, buttom, left, right)
        web_shot = self.get_web_shot()
        captcha = web_shot.crop((left, top, right, buttom))
        captcha.save('captcah.png')
        return captcha

    def get_points(self, captcha_result):
        """
        解析识别结果(json类型数据)
        :param captcha_result: 验证码识别结果
        :return: 图片坐标
        """
        groups = captcha_result.get('pic_str').split('|')
        locations = [[int(number) for number in group.split(',')] for group in groups]
        return locations

    def track_click_word(self, locations):
        """
        点击验证码对应图片
        :param locations:图片坐标
        :return:
        """
        for location in locations:
            element = self.get_12306_element()
            print(location)
            ActionChains(self.browser).move_to_element_with_offset(element, location[0], location[1]).click().perform()
            time.sleep(1)


    def login(self):
        btn = self.wait.until(EC.presence_of_element_located((By.ID, 'J-login')))
        btn.click()

    def isSuccess(self):
        """
        判断是否成功
        :return:
        """
        succ = False
        try:
            self.browser.find_element_by_id('loginSub')#还有登录按钮说明没有登录成功
            self.chaojiying.ReportError(self.pic_id)
        except :
            succ = True
        return succ

    def myCrack(self):
        """
        破解入口
        :return:
        """
        self.openWeb()#打开网页输入用户名密码
        captcha = self.get_captach_img() # 获得验证码图片
        bytes_array = BytesIO()
        captcha.save(bytes_array, format('png'))
        result = self.chaojiying.PostPic(bytes_array.getvalue(), CHAOJIYING_KIND)#识别验证码
        print(result)
        locations = self.get_points(result)
        self.track_click_word(locations)
        self.login()
        sus = self.isSuccess()
        if not sus:
            print('chengg')
        else:
            self.myCrack()

if __name__ == '__main__':
    myccc = Crack12306()
    myccc.myCrack()

