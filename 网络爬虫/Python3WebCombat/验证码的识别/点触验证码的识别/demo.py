import time
from io import BytesIO

from PIL import Image
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import sys
sys.path.append(r'C:\Users\Administrator\Desktop\python\Py_webSpider\Python3WebCombat\验证码的识别\点触验证码的识别\Chaojiying_Python\chaojiying_Python')
from chaojiying import Chaojiying_Client

USERNAME = 'sunlys'
PASSWORD = 'lys13788929721'
CHAOJIYING_USER = '13616859570'
CHAOJIYING_PSW = 'liyixin123'
CHAOJIYING_SOFT_ID = 900078
CHAOJIYING_KIND = 9102
class Crack12306:
    def __init__(self):
        self._url = 'https://kyfw.12306.cn/otn/login/init'
        self._browser = webdriver.Chrome()
        self._wait = WebDriverWait(self._browser, 20)
        self._username = USERNAME
        self._password = PASSWORD
        self._chaojiying = Chaojiying_Client(CHAOJIYING_USER, CHAOJIYING_PSW, CHAOJIYING_SOFT_ID)
        self._pic_id = None

    def __del__(self):
        self._browser.close()

    def open(self):
        """
        打开网页输入用户名密码
        :return: None
        """
        self._browser.get(self._url)
        username = self._wait.until(EC.presence_of_element_located((By.ID, 'username')))
        password = self._wait.until(EC.presence_of_element_located((By.ID, 'password')))
        username.send_keys(self._username)
        password.send_keys(self._password)

    def get_12306_element(self):
        """
        获取验证图片对象
        :return: 图片对象
        """
        element = self._wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.touclick .touclick-image')))
        return element

    def get_position(self):
        """
        获取验证码位置
        :return:  验证码位置元组
        """
        element = self.get_12306_element()
        time.sleep(2)
        location = element.location
        size = element.size
        top, bottom, left, right = location['y'], location['y'] + size['height'], \
                                   location['x'], location['x'] + size['width']
        return top, bottom, left, right

    def get_screen_shot(self):
        """
        获取网页截图
        :return:  截图对象
        """
        screen_shot = self._browser.get_screenshot_as_png()
        screen_shot = Image.open(BytesIO(screen_shot))
        return screen_shot

    def get_12306_image(self, name='captcha.png'):
        """
        获取验证码图片
        :return: 图片对象
        """
        top, bottom, left, right = self.get_position()
        print('验证码位置', top, bottom, left, right)
        screen_shot = self.get_screen_shot()
        captcha = screen_shot.crop((left, top, right, bottom))
        captcha.save(name)
        return captcha

    def get_points(self, captcha_result):
        """
        解析识别结果
        :param captcha_result: 识别结果
        :return: 转化后的结果
        """
        groups = captcha_result.get('pic_str').split('|')
        locations = [[int(number) for number in group.split(',')] for group in groups]
        return locations

    def touch_click_words(self, locations):
        """
        点击验证图片
        :param locations: 点击位置
        :return: None
        """
        element = self.get_12306_element()
        for location in locations:
            print(location)
            ActionChains(self._browser).move_to_element_with_offset(element, location[0], location[1]).click().perform()
            time.sleep(1)

    def login(self):
        """
        登录
        :return: None
        """
        submit = self._wait.until(EC.element_to_be_clickable((By.ID, 'loginSub')))
        submit.click()
        time.sleep(10)

    def check_login_success(self):
        """
        检查是否登录成功
        :return: None
        """
        success = False
        try:
            self._browser.find_element_by_id('loginSub')
            self._chaojiying.ReportError(self._pic_id)
        except NoSuchElementException:
            success = True
        return success

    def crack(self):
        """
        破解入口
        :return: None
        """
        self.open()

        # 获取验证码图片
        image = self.get_12306_image()
        bytes_array = BytesIO()
        image.save(bytes_array, format='PNG')

        # 识别验证码
        result = self._chaojiying.PostPic(bytes_array.getvalue(), CHAOJIYING_KIND)
        self._pic_id = result.get('pic_id')
        print(result)
        locations = self.get_points(result)
        self.touch_click_words(locations)

        # 登录
        self.login()

        # 失败后重试
        success = self.check_login_success()
        if not success:
            self.crack()
        else:
            print('登录成功')


if __name__ == '__main__':
    crack = Crack12306()
    crack.crack()