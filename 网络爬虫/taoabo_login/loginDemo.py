from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from selenium.webdriver.common.action_chains import ActionChains
#config

url = 'https://login.taobao.com/member/login.jhtml'             #网址
driver_path = r'C:\Users\Administrator\AppData\Local\Programs\Python\Python37\chromedriver.exe'     #驱动位置
option = webdriver.ChromeOptions()              #对象选项
# option.add_argument('--proxy-server=127.0.0.1:8080')
option.add_experimental_option('excludeSwitches',['enable-automation'])  #开发者模式

#浏览器对象
driver = webdriver.Chrome(executable_path=driver_path, options=option)
#设置对象等待时间
dwait = WebDriverWait(driver, 10)

def login(username, password):
    #打开网页
    driver.get(url)
    #密码登录----出现密码登录选项
    password_login = dwait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.forget-pwd.J_Quick2Static')))
    password_login.click()

    # 输入用户名密码
    input_username = dwait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.login-text.J_UserName')))
    input_username.send_keys(username)


    input_password = dwait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.pwd-field > span > .login-text')))
    input_password.send_keys(password)

    #登录
    but_login = dwait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#J_SubmitStatic')))
    # 点击一次 使滑块退出无线循环 并且清空密码
    but_login.click()
    time.sleep(3)

    #定位滑块
    slide = dwait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.tb-login')))
    # 平行移动鼠标，此处直接设一个超出范围的值，这样拉到头后会报错从而结束这个动作
    #点击鼠标左键，不松开
    ActionChains(driver).click_and_hold(slide).perform()
    for i in range(1,6):
        # action = ActionChains(driver).drag_and_drop_by_offset(slide, 50*i, 0).perform()
        ActionChains(driver).move_by_offset(xoffset=i*100, yoffset=0).perform()
        time.sleep(random.randint(1,3))
    #再次输入密码
    input_password = dwait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.pwd-field > span > .login-text')))
    input_password.send_keys(password)

    #再次登录
    but_login = dwait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#J_SubmitStatic')))
    but_login.click()


    name = dwait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.s-name')))
    print('your name :',name)

if __name__ == '__main__':
    username = "用户名"
    password = '密码'
    login(username, password)
