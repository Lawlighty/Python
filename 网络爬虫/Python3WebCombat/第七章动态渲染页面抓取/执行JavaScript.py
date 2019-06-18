from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://m.weibo.cn/p/index?containerid=2304132830678474_-_WEIBO_SECOND_PROFILE_WEIBO&luicode=10000011&lfid=2302832830678474')
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
for i in range(1,5):
    browser.execute_script('window.scrollTo(0, {})'.format(i*500))
    time.sleep(1)
browser.execute_script("alert('拉到底')")
time.sleep(1)



