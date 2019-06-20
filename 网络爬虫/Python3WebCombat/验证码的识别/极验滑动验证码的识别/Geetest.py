# 极验登录url = 'https://auth.geetest.com/login'
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from io import BytesIO
from PIL import Image
import time

class GrackGeettest():
    def __init__(self):
        self.email = 'testsssss@test.com'
        self.password = "123452226"
        self.url = 'https://auth.geetest.com/login'
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 10)

    def writeInfo(self):
        email = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#base > div.content-outter > div > div.inner-conntent > div:nth-child(3) > div > form > div:nth-child(1) > div > div > div > input')))
        email.send_keys(self.email)
        time.sleep(1)
        psw = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#base > div.content-outter > div > div.inner-conntent > div:nth-child(3) > div > form > div:nth-child(2) > div > div:nth-child(1) > div > input')))
        psw.send_keys(self.password)

    def get_geetest_btn(self):
        geetest_btn = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'captcha')))
        return geetest_btn

    def get_screenshot(self):
        """
        获取网页截图
        :return: 截图对象
        """
        screenshot = self.browser.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot))#ByresIO 封装
        return screenshot

    def get_position(self, full):
        """
        获取验证码位置
        :return: 验证码位置元祖
        """
        img = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME,'geetest_canvas_img ')))

        fullbg = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_canvas_fullbg ')))
        time.sleep(2)

        if full:
            self.browser.execute_script("arguments[0].setAttribute(arguments[1], arguments[2])", fullbg, "style", "")
        else:
            self.browser.execute_script("arguments[0].setAttribute(arguments[1], arguments[2])", fullbg, "style", "display: none")
        location = img.location#位置
        size= img.size
        top, bottom, left, right = location['y'], location['y'] + size['height'],location['x'],location['x']+size['width']
        return (top,bottom,left,right)


    def get_geetest_imgs(self, full, name='captcha.jpg', ):
        """
        获得验证码图片
        :param name: 图片名称
        :return: 图片对象
        """
        top, bottom, left, right = self.get_position(full)
        print('验证码位置',top, bottom, left, right)
        screenshot = self.get_screenshot()
        screenshot.save(name)
        captcha = screenshot.crop((left, top, right, bottom))#剪裁   左上右下的顺序
        return captcha

    def get_slider(self):
        """
        获取滑块
        :return:滑块对象
        """
        slider = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_slider_button')))
        return slider

    def is_pixel_equal(self, img1, img2,x, y):
        """
        判断两个像素是否相同
        :param img1: 图片
        :param img2:
        :param x: 位置
        :param y:
        :return: 是否相同
        """
        pixel1 = img1.load()[x, y]
        pixel2 = img2.load()[x, y]
        threshold = 60 #阈值
        if abs(pixel1[0]-pixel2[0])<threshold and abs(pixel1[1]-pixel2[1])<threshold and abs(pixel1[2]-pixel2[2])<threshold:
            return True
        else:
            return False

    def get_gap(self, img1, img2):
        """
        获得缺口偏移量
        :param img1: 完整图片
        :param img2: 有缺口图片
        :return:
        """
        left = 60 #缺口一般在滑块右边,直接忽略左边的一段位置
        for i in range(left, img1.size[0]):
            for j in range(img1.size[1]):
                if not self.is_pixel_equal(img1, img2, i, j):
                    left = i
                    return left

        return left


    def get_track(self, distance):
        """
        模拟滑块先加速再减速运动
        x :位移   v:当前速度
        x = v0 * t + 0.5 * a * t * t
        v = v0 + a * t
        :param distance: 偏移量
        :return: 运动轨迹列表
        """

        track = []#移动轨迹
        current = 0 #当前位移
        mid = distance*4/5 #减速阈值
        t = 0.2#计算时间
        v = 0#初速度

        while current<distance:
            if current<mid:
                a = 2  #加速度为+2
            else:
                a = -3 #加速度为-3
            v0 = v #初速度
            v = v0+a*t
            move = v0*t+1/2*a*t*t# 移动距离
            current = current+move
            track.append(round(move)) #返回浮点数x的四舍五入值
        return track

    def move_to_gap(self, slider, tracks):
        """
        拖动滑块到缺口处
        :param slider: 滑块
        :param tracks: 轨迹
        :return:
        """
        ActionChains(self.browser).click_and_hold(slider).perform()
        for x in tracks:
            ActionChains(self.browser).move_by_offset(xoffset=x, yoffset=0).perform()
        time.sleep(1)
        ActionChains(self.browser).release().perform()#释放


    def crack(self):
        self.browser.get(self.url)
        self.writeInfo()
        time.sleep(2)

        btn = self.get_geetest_btn()
        btn.click()

        img1 = self.get_geetest_imgs(full=True,name='fullPic.jpg')
        img2 = self.get_geetest_imgs(full=False,name='notfullPic.jpg')
        gap = self.get_gap(img1, img2)
        track = self.get_track(gap-1)
        slider = self.get_slider()
        self.move_to_gap(slider, track)
        time.sleep(1)

if __name__ == '__main__':
    myGrack = GrackGeettest()
    myGrack.crack()
