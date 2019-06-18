# 动作链的实现: 鼠标拖曳、键盘按键
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
time.sleep(1)
#切换frame
browser.switch_to_frame('iframeResult')
source = browser.find_element_by_css_selector('#draggable')
target = browser.find_element_by_css_selector('#droppable')
actions = ActionChains(browser)
actions.drag_and_drop(source,target)
#执行
actions.perform()

browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
browser.execute_script('alert("TO 到底了 wdnmd")')

time.sleep(3)
browser.close()