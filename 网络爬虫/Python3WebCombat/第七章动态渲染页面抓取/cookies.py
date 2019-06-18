from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
print('第一次Cookie:',browser.get_cookies())

browser.add_cookie({'name':'LLLyx','domain':'www.zhihu.com','value':'12306'})

print('第二次Cookie:',browser.get_cookies())

browser.delete_all_cookies()

print('第三次Cookie:',browser.get_cookies())


