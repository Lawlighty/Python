from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from bs4 import BeautifulSoup

html = '<div class="aa"><div class="BB"><a href="www.baidu.com"></div></div>'
soup = BeautifulSoup(html, 'html.parser')
href = soup.find('div',class_='BB').find('a')['href']
print(type(href))
print(href)