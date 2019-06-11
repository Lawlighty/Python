from selenium import webdriver

proxy = '112.85.167.44:9999'
options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=http://'+proxy)
driver = webdriver.Chrome(options=options)
driver.get('http://httpbin.org/get')