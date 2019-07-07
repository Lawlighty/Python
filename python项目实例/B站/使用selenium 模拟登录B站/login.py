from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import  By
from selenium.webdriver import ActionChains
from io import BytesIO
from PIL import Image
import time
import random

class LoginB():

    def __init__(self):
        """
        初始化
        """
        self.username = '13616859570'
        self.password = 'liyixin123'
        self.url = "https://www.bilibili.com/"
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 10)

    def opWeb_page(self):
        """
        打开网页
        :return:
        """
        self.browser.get(self.url)

    def get_loginPage(self):
        """
        进入登录页面
        :return:
        """
        ActionChains(self.browser).move_to_element(self.browser.find_element_by_class_name("i-face")).perform()
        login_btn = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "login-btn")))
        login_btn.click()
        time.sleep(3)

    def fill_out_info(self):
        """
        填写表单信息
        :return:
        """
        username = self.browser.find_element_by_id("login-username")
        password = self.browser.find_element_by_id("login-passwd")

        username.send_keys(self.username)
        time.sleep(1)
        password.send_keys(self.password)
        time.sleep(1)
        login_btn = self.browser.find_element_by_css_selector(".btn.btn-login")
        login_btn.click()


    def get_screenshot(self):
        """
        获得网页全屏截图
        :return: 截图
        """
        screenshot = self.browser.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot))
        return screenshot

    def get_Pic_location(self,fullbg):
        """
        获得验证码图片位置
        :param fullbg: 是否是完整验证码图片
        :return:
        """
        pic = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_canvas_slice')))
        pic2 = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_canvas_fullbg')))
        time.sleep(1)
        if fullbg:
            self.browser.execute_script("arguments[0].setAttribute(arguments[1], arguments[2])", pic2, "style", "")#设置图片缺口为""----得到完整图片
        else:
            self.browser.execute_script("arguments[0].setAttribute(arguments[1], arguments[2])", pic2, "style", "display: none")

        location = pic.location
        size = pic.size

        top, bottom, left, right = location['y'], location['y'] + size['height'],location['x'],location['x']+size['width']
        return top, bottom, left, right

    def get_Code_pic(self, fullbg=True, picName='aa.png'):
        """
        获得验证码图片
        :return: 验证码图片
        """
        top, bottom, left, right = self.get_Pic_location(fullbg)
        print('验证码位置', top, bottom, left, right)
        screenshot = self.get_screenshot()
        code_pic = screenshot.crop((left,top,right,bottom))
        code_pic.save(picName)
        print('图片保存成功')
        return code_pic

    def get_slider(self):
        """
        获得滑块
        :return:滑块对象
        """
        myslider = self.browser.find_element_by_class_name("geetest_slider_button")
        return myslider

    def pic_is_equal(self, img1, img2, x, y):
        """
        判断两张图片是否相同
        :param img1:
        :param img2:
        :param x:
        :param y:
        :return: 是否相同
        """
        p1 = img1.load()[x,y]
        p2 = img2.load()[x,y]
        threshold = 60  # 阈值
        # 两张图RGB的绝对值是否小于定义的阈值
        if abs(p1[1]-p2[1])<threshold and abs(p1[0]-p2[0])<threshold and abs(p1[2]-p2[2])<threshold:
            return True
        else:
            return False

    def get_Offset(self, img1, img2):
        """
        获得图片缺口偏移量
        :param img1:
        :param img2:
        :return: 偏移量
        """
        offset = 60 #初始偏移量
        for i in range(offset, img1.size[0]):#横向
            for j in range(img1.size[1]):#纵向
                if not self.pic_is_equal(img1,img2, i, j):
                    offset = i#横向偏移量
                    return offset

        return offset

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


    def Doit(self):
        self.opWeb_page()
        self.get_loginPage()
        self.fill_out_info()
        time.sleep(3)
        #完整验证码图片
        try:
            while self.browser.find_element_by_class_name('tit'):
                img1 = self.get_Code_pic(fullbg=True, picName="完整验证码图片.png")
                #残缺验证码图片
                img2 = self.get_Code_pic(fullbg=False, picName="残缺验证码图片.png")

                offset = self.get_Offset(img1,img2)
                track = self.get_track(offset-5)
                myslider = self.get_slider()
                self.move_to_gap(slider=myslider, tracks=track)
                time.sleep(3)
        except:
            print('登录成功')
            time.sleep(3)
            self.browser.close()

if __name__ == '__main__':
    a = LoginB()
    a.Doit()