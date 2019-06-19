from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')

input = browser.find_element_by_class_name('zu-top-add-question')
print(input.id)
print(input.location)
print(input.size)