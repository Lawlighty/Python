# 使用selenium 登录知乎
# url = 'https://www.zhihu.com/signup?next=%2F'
# url = 'https://www.zhihu.com/'
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#驱动位置
driverPath = r'C:\Users\Administrator\AppData\Local\Programs\Python\Python37\chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-automation'])

driver = webdriver.Chrome(executable_path=driverPath, options=options)
wait = WebDriverWait(driver, 10)
# driver.get(url='https://www.zhihu.com/signup?next=%2F')
driver.get(url='https://www.zhihu.com/')

#选择已有账号按钮-----------<div class="SignContainer-switch">已有帐号？<span>登录</span></div>
dengl = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.SignContainer-switch > span')))
dengl.click()
#进入账号密码登录模式
#单纯 账号密码输入会有 图片验证码出现
#使用绑定的  第三方(微博) 账号登录

shejiao_btn = driver.find_element_by_css_selector(".Button.Login-socialButtonEntrance.Button--plain")
shejiao_btn.click()
time.sleep(3)

weibo_src = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.Icon.Login-socialIcon.Icon--weibo')))
weibo_src.click()
time.sleep(3)
#进入微博登录页面
weibo_usen = driver.find_element_by_id('userId')
weibo_usen.send_keys('用户名')
time.sleep(3)
weibo_psw = driver.find_element_by_id('passwd')
weibo_psw.send_keys('密码')
time.sleep(3)
weibo_login = driver.find_element_by_css_selector(".WB_btn_login.formbtn_01")
weibo_login.click()
time.sleep(3)
#允许授权
allow_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".WB_btn_allow.formbtn_01")))
allow_btn.click()


