import requests
from bs4 import BeautifulSoup
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.17 Safari/537.36',
}
url = 'https://www.zhihu.com/signin?next=%2F'

try:
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.prettify())
except Exception as  e:
    print(e)

