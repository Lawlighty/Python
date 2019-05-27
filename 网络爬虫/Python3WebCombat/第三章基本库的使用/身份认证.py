# 打开网页需要身份认证
import requests
from requests.auth import HTTPBasicAuth
import re
url = 'www.taobao.com'
# r = requests.get(url, HTTPBasicAuth=('username', 'password'))或者
r = requests.get(url,auth=('username', 'password'))
print(r.status_code)

